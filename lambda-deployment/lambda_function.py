from __future__ import print_function

import json
import os
import requests


def lambda_handler(event, context):
    headers = {
        'content-type': 'application/json'
    }
    image_path = os.environ['image_path']
    api_url = os.environ['api_url']
    for record in event['Records']:
        
        bucket = record['s3']['bucket']['name']
        key_name = record['s3']['object']['key']
        image_id = key_name.split('_')[0]
        print(bucket, key_name, image_id)

        response = requests.request(
            'PATCH', 
            '{}/{}/'.format(api_url, image_id), 
            headers=headers,
            json={
        	   'url': '{}/{}'.format(image_path, key_name)
            }
        )
