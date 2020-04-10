import boto3
import json
import pprint
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
response = ec2.describe_instances()
demo = ec2.describe_instances(Filters=[{'Name':'tag:Name','Values':['demo-instance']}])
print(demo)
