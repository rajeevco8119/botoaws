import boto3
from botocore.exceptions import ClientError
import json
import pprint
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
try:
    response = ec2.describe_security_groups(GroupIds=['SECURITY_GROUP_ID'])
    print(response)
except ClientError as e:
    print(e)
