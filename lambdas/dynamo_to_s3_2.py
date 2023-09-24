import json


def lambda_handler(event, context):
    print("Came here inside lambda")
    print("Event is: " , event)
    body = {
        "message": "Successful Execution",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}