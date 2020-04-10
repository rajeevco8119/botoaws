import boto3
from botocore.exceptions import ClientError
def change_instance_security_group(instance_id,security_group_id):
    ec2_client = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        print(response)
    except ClientError as e:
        print(e)
        return False
change_instance_security_group()
