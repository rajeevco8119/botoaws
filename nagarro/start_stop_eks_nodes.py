import sys

import boto3
import json

min_node_count = sys.argv[1]
max_node_count = sys.argv[2]
desired_node_count = sys.argv[3]
clusterName = sys.argv[4]

session = boto3.Session(profile_name='GSSC-Test')

client = session.client('eks')


def describe_cluster(clusterName):
    response = client.describe_cluster(
        name=clusterName
    )
    print(response)
    return response['cluster']['arn']


def list_nodegroup(clusterName):
    response = client.list_nodegroups(
        clusterName=clusterName
    )
    return response['nodegroups'][0]


def get_flag():
    flag = client.list_tags_for_resource(
        resourceArn=describe_cluster(clusterName=clusterName)
    )
    skip_automatic_stop = flag['tags']['--skip-automatic-stop']
    return skip_automatic_stop


def update_cluster():
    response = client.update_nodegroup_config(
        clusterName=clusterName,
        nodegroupName=list_nodegroup(clusterName),
        scalingConfig={
            'minSize': int(min_node_count),
            'maxSize': int(max_node_count),
            'desiredSize': int(desired_node_count)
        }
    )
    print(response['update']['status'])


if str(get_flag()) in ['no', 'NO', 'No']: # rds stop and desired count=0
    print('Updating cluster...')
    update_cluster()
else:
    print('Flag "Skip automatic stop" is set to True...Hence not updating cluster')
