import boto3
import json 

def store_in_S3(data, s3_bucket, s3_key):
    try:
        print("Here in the store data in S3 function.")
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Bucket = s3_bucket,
            Key = s3_key,
            Body = json.dumps(data),
            ContentType = 'application/json'
        )
        print("Insert in S3 success")
    except Exception as e:
        print('Error Occurred in store function: ', str(e))