import boto3
import json

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_SESSION_TOKEN = ""
AWS_REGION = 'eu-west-1'

client = boto3.client('eks', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      aws_session_token=AWS_SESSION_TOKEN,
                      region_name=AWS_REGION)


def list_clusters():
    response = client.list_clusters()
    print(json.dumps(response["clusters"], indent=2))


def describe_cluster(cluster):
    response = client.describe_cluster(name=cluster)
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
                          region_name=AWS_REGION)
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
                          region_name=AWS_REGION)
    response = client.describe_security_groups()['SecurityGroups']
    response = json.dumps(response, indent=4, sort_keys=True, default=str)
    print(response)


def get_launch_template(instanceid):
    response = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            aws_session_token=AWS_SESSION_TOKEN,
                            region_name=AWS_REGION)
    data = response.get_launch_template_data(InstanceId=instanceid)
    print(json.dumps(data, indent=4, sort_keys=True, default=str))


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

def create_nodegroup(cluster, nodegroup, minsize, maxsize, desiredsize, subnets, noderole, launchtemplate_name,
                     launchtemplate_id):
    response = client.create_nodegroup(
        clusterName=cluster,
        nodegroupName=nodegroup,
        scalingConfig={
            'minSize': minsize,
            'maxSize': maxsize,
            'desiredSize': desiredsize
        },
        subnets=subnets,
        nodeRole=noderole,
        launchTemplate={
            'id': launchtemplate_id
        },
        capacityType='ON_DEMAND'
    )
    print(json.dumps(response, indent=4, sort_keys=True, default=str))
    return

# list_nodegroups('mytestcluster')
# describe_cluster('mytestcluster')
# getIAMRoles()
# get_subnets('vpc-0456d8c89e0facd9f')

# list_clusters()
# describe_cluster(cluster='oss-stage')
# createCluster('test_cluster_boto3', 'arn:aws:iam::2425225233522:role/eksctl-oss-stage-cluster-ServiceRole-15XOY3YRCZQVU',
#               get_subnets('vpc-0456d8c89e0facd9f'), ['sg-0dd6b8ace144b0daf'])

# subnet_ng = ['subnet-05b3aa4eae881f072', 'subnet-00a4718fafab5626f']
# 
# create_nodegroup('test_cluster_boto3','test_cluster_boto3_ng',1,1,1,
#                  subnet_ng,'arn:aws:iam::474551112000:role/eksctl-oss-stage-nodegroup-oss-st-NodeInstanceRole-VLIOH4NRUAAS',
#                  'eksctl-oss-stage-nodegroup-oss-stage-ng','lt-0d8f877cc54a89f90')

# describe_security_group()
# delete_cluster('test_cluster_boto3')

# get_launch_template('i-0361768edb6fffbfb')
