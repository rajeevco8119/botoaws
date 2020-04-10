import sys
import boto3
from botocore.exceptions import ClientError
instance_id = 'INSTANCE_ID'
#action = 'ON'
action = 'OFF'
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
if action=='ON':
    try:
        ec2.start_instances(InstanceIds=[instance_id],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    try:
        response = ec2.start_instances(InstanceIds=[instance_id],DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
