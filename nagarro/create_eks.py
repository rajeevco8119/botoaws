import boto3
import json

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_SESSION_TOKEN = ""

client = boto3.client('eks', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      aws_session_token=AWS_SESSION_TOKEN,
                      region_name='eu-west-1')


def list_clusters():
    response = client.list_clusters()
    print(json.dumps(response["clusters"], indent=2))


def describe_cluster(cluster):
    response = client.describe_cluster(
        name=cluster
    )
    json_response = json.dumps(response, indent=4, sort_keys=True, default=str)
    print(json_response)


def list_nodegroups(cluster):
    response = client.list_nodegroups(
        clusterName=cluster
    )
    print(json.dumps(response, indent=2))


def get_subnets(vpcid):
    client = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          aws_session_token=AWS_SESSION_TOKEN,
                          region_name='eu-west-1')
    vpcs = []
    subnets = []
    for vpc in range(len(client.describe_vpcs()['Vpcs'])):
        vpcs.append(client.describe_vpcs()['Vpcs'][vpc]['VpcId'])
    if vpcid not in vpcs:
        print('Vpcid doesn"t exist')
        exit()
    else:
        for subnet in range(len(client.describe_subnets()['Subnets'])):
            if client.describe_subnets()['Subnets'][subnet]['VpcId'] == vpcid:
                subnets.append(client.describe_subnets()['Subnets'][subnet]['SubnetId'])
    return subnets


def describe_security_group():
    client = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          aws_session_token=AWS_SESSION_TOKEN,
                          region_name='eu-west-1')
    response = client.describe_security_groups()['SecurityGroups']
    response = json.dumps(response, indent=4, sort_keys=True, default=str)
    print(response)


def createCluster(clustername, arn, subnetid, security_grp_id,
                  cidr=None, endpoint_public=False, endpoint_private=True):
    response = client.create_cluster(
        name=clustername,
        roleArn=arn,
        resourcesVpcConfig={
            'subnetIds': subnetid,
            'securityGroupIds': security_grp_id,
            'endpointPublicAccess': endpoint_public,
            'endpointPrivateAccess': endpoint_private
        }
    )
    print(response)

def delete_cluster(clusterName):
    response = client.delete_cluster(
        name=clusterName
    )
    print(response)

# By default AWS managed policy- "AmazonEKSClusterPolicy" is assigned to role for which RoleARN is assigned

# list_nodegroups('mytestcluster')
# describe_cluster('mytestcluster')
# get_subnets(vpcname)

# list_clusters()
# describe_cluster(cluster='oss-stage')
# createCluster('test_cluster_boto3', 'arn',
#               get_subnets('vpc-id'), ['sg-name'])

# describe_security_group()
# delete_cluster(clusterName='oss-stage')

