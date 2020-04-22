import boto3

s3 = boto3.client('s3',aws_access_key_id='AKIA4M5FRLANPLU3JFA5',
                        aws_secret_access_key='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')
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print('Bucket list %s' % buckets)
