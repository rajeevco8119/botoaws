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

client = boto3.client('eks', aws_access_key_id='ASIAW47LTKFAMSY27FKX',
                      aws_secret_access_key='gOzKwm9+VQM/ukuLc3lV84L9OMsebRZvuRZerG0L',
                      aws_session_token="IQoJb3JpZ2luX2VjEE8aCWV1LXdlc3QtMSJIMEYCIQDLoDJFMed3MsOvE5hV5Ye68CDd3XzKEf6NZLRzndJigQIhANpVGgRmOOkljUrxkZmC9Qzu6oibKTELQB3cxk1S/RhlKqsDCOj//////////wEQABoMNDc0NTUxMTEyMDAwIgwizyIN4c4YIBEZo3Aq/wLD8BNO5FJPXIozJrEcJXWQhCJHd58XIsI3Isn1a/R25YXliQMfuhz2Ct6oViwpGd4SGzMHYbVLDQgYBbthL6BF04Np6E0OvxRT6tsKJKnmK2jEqnRcPPplv4eok6PXzUnGcvdbSVDRhq5S10FjNugmC2et6lMti5kAgSL0dN+W4n9kBDiy3yS2v2JrDUZ4gGOPJ/RTqs5O92SHTFevf+f4INcb5afRV8UrsndvkzNQLjze8ragzrMj+ZtfKWtqkygWRSyUDe2PZAmOjTTUGmLQvFKKdbpSvenJOiSS9vYIJ9jjTWqp5k11UN8/FAdyeXte9XjG9A8njL1zcrySTI2as1lWLGHkIsWsO2OYgBy2l03gTE4Ijqs6HZS9iznHhxhu16R1iZ7pKEdmzsSQ3MxLO8qFVTQhDVe2WR80EI5o/oL1YAdGIoacvRx9FGQb9Je/JfvEr3gTB/586FgEjnBpgoD3wbF6HD1idD8Vvf7X2ml/VgHiolopNfdjgbsYXzDds5CZBjqlAbjSvKdMGbHtiLE6hrN+qDQOzOIuc2ezqbVQ2Jr/ni+oCzjtzlKVGA8FLkd4mRgeDnXFcdMltBDNThjFbx7hLKkx/NNuAdEJY0cSmEKPFgDXLd/hTeDNV+nYGrVMaWHdmqtnsbEJnvCTjzH9ASCI9g9nlTCIofAyGIWL9UleNnfMpRtUm6CnqktusqPrSqtN1YBFQuSREwMzEX21mAOGQsz8CV2T6g==",
                      region_name='eu-west-1')

client2 = boto3.client('rds', aws_access_key_id='ASIAW47LTKFAMSY27FKX',
                       aws_secret_access_key='gOzKwm9+VQM/ukuLc3lV84L9OMsebRZvuRZerG0L',
                       aws_session_token="IQoJb3JpZ2luX2VjEE8aCWV1LXdlc3QtMSJIMEYCIQDLoDJFMed3MsOvE5hV5Ye68CDd3XzKEf6NZLRzndJigQIhANpVGgRmOOkljUrxkZmC9Qzu6oibKTELQB3cxk1S/RhlKqsDCOj//////////wEQABoMNDc0NTUxMTEyMDAwIgwizyIN4c4YIBEZo3Aq/wLD8BNO5FJPXIozJrEcJXWQhCJHd58XIsI3Isn1a/R25YXliQMfuhz2Ct6oViwpGd4SGzMHYbVLDQgYBbthL6BF04Np6E0OvxRT6tsKJKnmK2jEqnRcPPplv4eok6PXzUnGcvdbSVDRhq5S10FjNugmC2et6lMti5kAgSL0dN+W4n9kBDiy3yS2v2JrDUZ4gGOPJ/RTqs5O92SHTFevf+f4INcb5afRV8UrsndvkzNQLjze8ragzrMj+ZtfKWtqkygWRSyUDe2PZAmOjTTUGmLQvFKKdbpSvenJOiSS9vYIJ9jjTWqp5k11UN8/FAdyeXte9XjG9A8njL1zcrySTI2as1lWLGHkIsWsO2OYgBy2l03gTE4Ijqs6HZS9iznHhxhu16R1iZ7pKEdmzsSQ3MxLO8qFVTQhDVe2WR80EI5o/oL1YAdGIoacvRx9FGQb9Je/JfvEr3gTB/586FgEjnBpgoD3wbF6HD1idD8Vvf7X2ml/VgHiolopNfdjgbsYXzDds5CZBjqlAbjSvKdMGbHtiLE6hrN+qDQOzOIuc2ezqbVQ2Jr/ni+oCzjtzlKVGA8FLkd4mRgeDnXFcdMltBDNThjFbx7hLKkx/NNuAdEJY0cSmEKPFgDXLd/hTeDNV+nYGrVMaWHdmqtnsbEJnvCTjzH9ASCI9g9nlTCIofAyGIWL9UleNnfMpRtUm6CnqktusqPrSqtN1YBFQuSREwMzEX21mAOGQsz8CV2T6g==",
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
