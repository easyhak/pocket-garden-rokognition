import json
import boto3

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

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':name}},
    MaxLabels=10,
        # Uncomment to use image properties and filtration settings
        #Features=["GENERAL_LABELS", "IMAGE_PROPERTIES"],
        #Settings={"GeneralLabels": {"LabelInclusionFilters":["Cat"]},
        # "ImageProperties": {"MaxDominantColors":10}}
    )
    resArr = []
    for x in response['Labels']:
        resArr.append(x['Name'])
    return resArr
    

