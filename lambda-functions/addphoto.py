import json
import boto3  
import time
import datetime

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('LeaguesGallery')

def lambda_handler(event, context):
    username=event['body-json']['username']
    leagueName=event['body-json']['leagueName']
    tags=event['body-json']['tags']
    ts=time.time()
    timestamp=int(ts*1000)
    leagueID=str(timestamp)
    
    table.put_item(
    Item={                        
            "LeagueID": leagueID,
            "LeagueName": leagueName,
            "OwnerUserId": username,
            "Tags": tags,
            #"ExifData": ExifData
        }
    )
                
    return {
        "statusCode": 200,
        "body": json.dumps(photoID)
    }
    
    
    
