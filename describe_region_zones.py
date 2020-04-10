import boto3
ec2 = boto3.client('ec2',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY',region_name='us-east-2')
response = ec2.describe_regions()
print('Regions:',response['Regions'])
response = ec2.describe_availability_zones()
print('Availability Zones:',response['AvailabilityZones'])
