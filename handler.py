import json
import pandas as pd


def greeting(event, context):
    dummy = pd.DataFrame({"name": ['jinung'], "age": [27]})

    return {
        'statusCode': 200,
        'body': json.dumps({"greeting": 'Hello from lambda, This API Deployed from serverless framework & Github Actions!!!', 
        "data": dummy})
    }
