import boto3
import json
from botocore.exceptions import ClientError
SECURITY_GROUP_NAME = 'launch-wizard-2'
DESCRIPTION = 'launch-wizard-1 created 2020-01-20T13:44:52.208+05:30'
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
#print(vpc_id)
try:
    response = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME,Description=DESCRIPTION,VpcId=vpc_id)
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
    data = ec2.authorize_security_group_ingress(GroupId=security_group_id,
                                                IpPermissions=[
                                                    {'IpProtocol':'tcp',
                                                     'FromPort':80,
                                                     'ToPort':80,
                                                     'IpRanges':[{'CidrIp':'0.0.0.0/0'}]},
                                                    {'IpProtocol': 'tcp',
                                                     'FromPort': 22,
                                                     'ToPort': 22,
                                                     'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
                                                ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)
