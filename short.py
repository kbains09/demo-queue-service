# for short polling messages
import json
import boto3

#SQS queue URL
queueURL = 'https://sqs.us-east-1.amazonaws.com/892724857555/MyQueue'

#Create an SQS client
client = boto3.client('sqs',region_name='us-east-1',aws_access_key_id="AKIA47WUMJLJ6DMFW7QI",
         aws_secret_access_key= "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")

#Delete all messages in the queue
delete_response = client.purge_queue(
    QueueUrl=queueURL
)

#Receive messages from the queue
response = client.receive_message(
    QueueUrl=queueURL,
    AttributeNames=['All'],
    WaitTimeSeconds=0
)

#Send a message to queue
send_response = client.send_message(
    QueueUrl=queueURL,
    MessageAttributes={
        'Subject': {
            'DataType': 'String',
            'StringValue': 'Sample Message'
        },
    },
    MessageBody=(
        'This message will not be received during short polling'
    )
)

#Print the message received
print(response.get('Messages'))