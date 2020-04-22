import boto3

s3 = boto3.client('s3',aws_access_key_id='AKIA4M5FRLANPLU3JFA5',
                        aws_secret_access_key='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')
filename = 'wp.jpg'
bucket_name = 'rajco819'
s3.upload_file(filename,bucket_name,filename)