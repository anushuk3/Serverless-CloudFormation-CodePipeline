import boto3
import os
import json


def lambda_handler(event, context):
    print ('Inserting data in the table')

    # Instantiate a table resource object without actually creating a DynamoDB table.
    # Note that the attributes of this table are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes on the table resource are accessed or its load() method is called.

    dynamodb = boto3.resource ('dynamodb')
    table = dynamodb.Table (os.environ['DB_TABLE_NAME'])
    table.put_item (
        Item={
            'category': category,
            'course': course,
            'description': description,
            'fee': fee
        }
    )
    return dict (
        statusCode=200,
        body=json.dumps (event)
    )