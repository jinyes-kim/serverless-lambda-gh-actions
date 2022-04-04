import json


def greeting(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda, This API Deployed from serverless framework & Github Actions')
    }
