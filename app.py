import urllib.parse
from deepracer.boto3_enhancer import deepracer_client
import os


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    model_name = key.partition('/')[0]
    dr_client = deepracer_client()
    model_arn = dr_client.import_model(Type='REINFORCEMENT_LEARNING',
                                       Name=model_name,
                                       ModelArtifactsS3Path='s3://{}/{}'.format(bucket, model_name),
                                       RoleArn=os.environ['importRoleArn'])
    print('A DeepRacer model {} was imported successfully'.format(model_arn))
