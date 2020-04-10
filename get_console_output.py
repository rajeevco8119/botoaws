import boto3
import sys
def get_console_output(instance_id):
    ec2 = boto3.resource('ec2', aws_access_key_id='ACCESS_KEY',
                       aws_secret_access_key='SECRET_KEY', region_name='us-east-2')
    ec2_instance = ec2.Instance(instance_id)
    json_output = ec2_instance.console_output()
    return json_output.get('Output','')
instance_id = 'INSTANCE_ID'
print(get_console_output(instance_id))
