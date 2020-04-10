import boto3
from botocore.exceptions import ClientError
def create_ec2_instance(image_id, instance_type, keypair_name):
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        print(e)
        return
    return response['Instances'][0]
def main():
    image_id = 'AMI_IMAGE_ID'
    instance_id = 'INSTANCE_TYPE'
    keypair_name = 'KEYPAIR_NAME'
    instance_info = create_ec2_instance(image_id,instance_id,keypair_name)
    if instance_info is not None:
        print('Launched EC2 Instance: '+instance_info["InstanceId"])
        print('VPC ID: ' + instance_info["VpcId"])
        print('Private IP Address:' + instance_info["PrivateIpAddress"])
        print('Current State' + instance_info["State"]["Name"])
if __name__=='__main__':
    main()
