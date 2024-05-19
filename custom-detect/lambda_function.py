import json
import boto3
import os

rekognition_arn = os.environ['rekognition_arn']

model = rekognition_arn
min_confidence=95

def lambda_handler(event, context):
    print(event)
    print(context)
    data = json.loads(event['body'])
    bucket = data["bucket"]
    name = data["name"]
    # bucket = event["bucket"]
    # name = event["name"]
    print(bucket)
    print(name)
    session = boto3.Session(region_name='ap-northeast-2')
    client = session.client('rekognition')

    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': name}},
        MinConfidence=2,
        ProjectVersionArn=model
        # Uncomment to use image properties and filtration settings
         #Features=["GENERAL_LABELS", "IMAGE_PROPERTIES"],
         #Settings={"GeneralLabels": {"LabelInclusionFilters":["Cat"]},
         # "ImageProperties": {"MaxDominantColors":10}}
    )
    print(response)
    
    # 이름만 출력
    return response['CustomLabels'][0]["Name"]
    
