import boto3

# Create an SQS client
client = boto3.client('sqs',region_name='us-east-1',aws_access_key_id="AKIA47WUMJLJ6DMFW7QI",
         aws_secret_access_key= "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")

# URL of the queue
queue_url = 'https://sqs.us-east-1.amazonaws.com/892724857555/MyQueue

# Send message to SQS queue
response = client.send_message(
    QueueUrl=queue_url,
    MessageAttributes={
        'Subject': {
            'DataType': 'String',
            'StringValue': 'Sample Message'
        },
    },
    MessageBody=(
        'This is a sample message'
    )
)

print(response['MessageId'])