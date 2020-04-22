import boto3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import json
from botocore.exceptions import ClientError

bucket_name_in_default_region = 'raj'
bucket_name_in_specified_region = 'raj'
REGION_NAME = 'Global'

d = datetime.datetime.now()
Current_time = "{}{}{}".format(d.month,d.day,d.year)

import boto3
def create_bucket(bucket_name,region=REGION_NAME):
    try:
        if region is None:
            s3_client = boto3.resource('s3',aws_access_key_id='AKIA4M5FRLANPLU3JFA5',
                        aws_secret_access_key='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')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.resource('s3',aws_access_key_id='AKIA4M5FRLANPLU3JFA5',
                        aws_secret_access_key='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')
            location = {'LocationConstraint':region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        print(e)
        return False
    return True
print(create_bucket('rajco819','us-west-2'))
# def main():
#     bucket_name_in_default_region = 'BUCKET_NAME'
#     bucket_name_in_specified_region = 'BUCKET_NAME'
#     region = 'us-west-2'
#     if create_bucket(bucket_name_in_default_region):
#         print('Bucket created in default region')
#
#     if create_bucket(bucket_name_in_specified_region,region):
#         print('Bucket created in specified region')
