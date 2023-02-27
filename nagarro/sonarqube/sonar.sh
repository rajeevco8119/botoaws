vm.max_map_count=262144
fs.file-max=65536
ulimit -n 65536
ulimit -u 4096

cat >> /etc/security/limits.conf << EOF
sonarqube   -   nofile   65536
sonarqube   -   nproc    4096
EOF

sudo amazon-linux-extras install java-openjdk11 -y
sudo yum install java-1.8.0-openjdk -y
sudo yum update -y
sudo amazon-linux-extras enable postgresql14
sudo yum install postgresql-server -y
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql

echo postgres:myPassword | chpasswd
su - postgres 
createuser sonar
psql
ALTER USER sonar WITH ENCRYPTED PASSWORD 'PWORD';
CREATE DATABASE sonarqube OWNER sonar;
GRANT ALL PRIVILEGES ON DATABASE sonarqube to sonar;
\q
exit
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-8.6.1.40680.zip
sudo yum install zip -y
unzip sonarqube*.zip
rm -rf *.zip
mv sonar* /opt/sonarqube
sudo groupadd sonar
sudo useradd -c "SonarQube - User" -d /opt/sonarqube/ -g sonar sonar
sudo chown -R sonar:sonar /opt/sonarqube/
sudo nano /opt/sonarqube/conf/sonar.properties


cat >> /opt/sonarqube/conf/sonar.properties << EOF
sonar.jdbc.username=sonar
sonar.jdbc.password=PASSWORD
sonar.jdbc.url=jdbc:postgresql://localhost/sonarqube
sonar.search.javaOpts=-Xmx512m -Xms512m -XX:MaxDirectMemorySize=256m -XX:+HeapDumpOnOutOfMemoryError
sonar.web.host=SERVER
sonar.web.port=9000
sonar.web.javaAdditionalOpts=-server
sonar.search.javaOpts=-Xmx512m -Xms512m -XX:+HeapDumpOnOutOfMemoryError
sonar.log.level=INFO
sonar.path.logs=logs
EOF

cat >> /etc/systemd/system/sonarqube.service <<EOF
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
User=sonar
Group=sonar
Restart=always
LimitNOFILE=65536
LimitNPROC=4096

[Install]
WantedBy=multi-user.target

EOF

sudo systemctl start sonarqube
sudo systemctl enable sonarqube

sudo amazon-linux-extras install nginx1
sudo systemctl start nexus
sudo systemctl enable nexus

cat >>  /etc/nginx/sites-enabled/sonarqube.conf << EOF
server{
 
listen      8080;
server_name 18.202.19.186;
access_log  /var/log/nginx/sonar.access.log;
error_log   /var/log/nginx/sonar.error.log;
proxy_buffers 16 64k;
proxy_buffer_size 128k;
 
location / {
proxy_pass  http://127.0.0.1:9000;
proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
proxy_redirect off;
proxy_set_header    Host            $host;
proxy_set_header    X-Real-IP       $remote_addr;
proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header    X-Forwarded-Proto http;
}
}

EOF 
