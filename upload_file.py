import boto3

s3 = boto3.client('s3',aws_access_key_id='AWS_ACCESS_KEY',
                        aws_secret_access_key='AWS_SECRET_KEY')
filename = 'wp.jpg'
bucket_name = 'rajco819'
s3.upload_file(filename,bucket_name,filename)
