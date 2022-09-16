import sys

import boto3
import json

min_node_count = 0
max_node_count = 1
desired_node_count = 0
clusterName = 'oss-stage'

client = boto3.client('eks', aws_access_key_id='<access-id>',
                      aws_secret_access_key='<secret-key>',
                      aws_session_token="<session-token>",
                      region_name='<region-name>')


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
            'minSize': min_node_count,
            'maxSize': max_node_count,
            'desiredSize': desired_node_count
        }
    )
    print(response['update']['status'])


if str(get_flag()) in ['no', 'NO', 'No']:
    print('Updating cluster...')
    update_cluster()
else:
    print('Flag "Skip automatic stop" is set to True...Hence not updating cluster')
