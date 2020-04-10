import boto3
from botocore.exceptions import ClientError
def terminate_instances(instance_ids):
    ec2 = boto3.client('ec2', aws_access_key_id='ACCESS_KEY',
                       aws_secret_access_key='SECRET_KEY', region_name='us-east-2')
    try:
        states = ec2.terminate_instances(InstanceIds=instance_ids)
    except ClientError as e:
        return None
    return states['TerminatingInstances']
