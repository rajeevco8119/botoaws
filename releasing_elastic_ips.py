import boto3
from botocore.exceptions import ClientError
ALLOCATION_ID = ''
ec2 = boto3.client('ec2', aws_access_key_id='ACCESS_KEY',
                       aws_secret_access_key='SECRET_KEY', region_name='us-east-2')
try:
    response = ec2.release_address(AllocationId=ALLOCATION_ID)
    print('Address released')
except ClientError as e:
    print(e)
