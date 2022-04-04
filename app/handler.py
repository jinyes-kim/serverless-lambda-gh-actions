import json
import pandas as pd


def greeting(event, context):
    df= pd.DataFrame({"name": ["jinung"], "age": [27]})
    dummy = df.to_json(orient='index')

    return {
        'statusCode': 200,
        'body': json.dumps({"greeting": 'Hello from lambda, This API Deployed from serverless framework & Github Actions!!!', 
        "data": dummy})
    }
