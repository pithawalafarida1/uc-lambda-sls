import json
from lambdas.HelperFunctions.FormattedDate import FormattedDate
from lambdas.HelperFunctions.StoreInS3 import store_in_S3

def eventHandler(event):
    formatted_date =  FormattedDate()
    s3_bucket = 's3objectbucket'
    s3_key = 'data/' + formatted_date + '.json'
    for record in event['Records']:
        event_name= record['eventName']
        print(event_name)
        if event_name == 'INSERT' or event_name == 'MODIFY':
            data= record['dynamodb']['NewImage']
            store_in_S3(data, s3_bucket, s3_key)
        elif event_name == 'REMOVE':
            data= record['dynamodb']['OldImage']
            store_in_S3(data, s3_bucket, s3_key)
    body = {
            "message": "Successful Execution",
            "input": event,
        }
    return {"statusCode": 200, "body": json.dumps(body)}