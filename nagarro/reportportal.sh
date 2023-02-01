#https://reportportal.io/docs/Deploy-with-Docker
#!/bin/bash
sudo yum update
sudo yum install docker -y
sudo usermod -a -G docker ec2-user
sudo yum install python3-pip
export PATH=$PATH:/usr/local/bin >> ~/.bashrc 
. ~/.bashrc
sudo pip3 install docker-compose
sudo systemctl enable docker.service
sudo systemctl start docker.service
docker version
docker-compose version
curl -LO https://raw.githubusercontent.com/reportportal/reportportal/master/docker-compose.yml
export PATH=$PATH:/usr/local/bin
mkdir -p data/elasticsearch
chmod 777 data/elasticsearch
chgrp 1000 data/elasticsearch

cat >> /etc/sysctl.conf << EOF
vm.max_map_count=262144
EOF
sysctl -w vm.max_map_count=262144
 

docker-compose -p reportportal up -d --force-recreate
echo "Default User: default\1q2w3e Administrator: superadmin\erebus"
