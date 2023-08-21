import boto3
import warnings

warnings.filterwarnings("ignore")

region = 'ap-southeast-1'
ec2_client = boto3.client("ec2", region_name=region)
sns_client = boto3.client("sns", region_name=region)

topic_arn = 'arn:aws:sns:ap-southeast-1:642126786835:utils'
msg = 'test string'
sub = 'test'


def publish_to_sns(msg, sub, topic_arn):
    topic_arn = topic_arn
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=msg,
        Subject=sub
    )
    print(response)


publish_to_sns(msg, sub, topic_arn)
