import boto3
KEY_PAIR_NAME = 'test'
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
response = ec2.create_key_pair(KeyName=KEY_PAIR_NAME)
print(response)
#Just give the keypair name and boto3 has function create_key_pair to create the keypair
