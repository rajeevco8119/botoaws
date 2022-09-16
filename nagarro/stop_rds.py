import sys

# s3 = session.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

# response = s3.list_buckets()
# buckets = [bucket['Name'] for bucket in response['Buckets']]
# print('Bucket list %s' % buckets)
import boto3

cluster_name= 'oss-stage'
db_name = 'blackduck-db'

client = boto3.client('eks', aws_access_key_id='',
                      aws_secret_access_key='',
                      aws_session_token="",
                      region_name='eu-west-1')

client2 = boto3.client('rds', aws_access_key_id='',
                       aws_secret_access_key='',
                       aws_session_token="",
                       region_name='eu-west-1')



def list_nodegroup(clusterName):
    response = client.list_nodegroups(
        clusterName=clusterName
    )
    return response['nodegroups'][0]


def get_desired_nodegroup_count(clusterName):
    response = client.describe_nodegroup(
        clusterName=clusterName,
        nodegroupName=list_nodegroup(clusterName=clusterName)
    )
    return response['nodegroup']['scalingConfig']['desiredSize']


def rds_action(clusterName):
    desired_count = get_desired_nodegroup_count(clusterName=clusterName)
    if desired_count == 0:
        stop_rds()


def stop_rds():
    response2 = client2.stop_db_instance(
        DBInstanceIdentifier=db_name
    )

rds_action(cluster_name)
