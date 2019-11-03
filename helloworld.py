def lambda_handler(event, context):
    print("Inside lambda handler")

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },s
        "body": "Hello World!"
    }

    return resp