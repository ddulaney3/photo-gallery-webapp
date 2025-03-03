import json
import boto3  

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table('LeaguesGallery')

def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']

    return {
        "statusCode": 200,
        "body": items
    }
