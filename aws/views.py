import boto
import uuid

from django.conf import settings

from .models import Image


def create_connection_to_s3():
    if hasattr(settings, 'S3_API_KEY'):
        api_key = settings.S3_API_KEY
        secret_key = settings.S3_SECRET_KEY
        host = settings.AWS_S3_HOST
        return boto.connect_s3(api_key, secret_key, host=host)
    return boto.connect_s3()

s3_connection = create_connection_to_s3()


def get_signed_upload_url():
    bucket = settings.AWS_STORAGE_BUCKET_NAME
    image = Image.objects.create()
    filename = '{}_{}.jpg'.format(image.id, uuid.uuid4())
    signed_upload = s3_connection.generate_url(5*60, 'PUT', bucket, filename, headers={'Content-Type': 'image/jpeg'})
    return signed_upload

