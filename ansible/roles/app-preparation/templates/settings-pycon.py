# -*- coding: utf8 -*-

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ django_secret_key }}'
DEBUG = False
STATIC_ROOT = '{{ web_base_dir }}/STATIC/static'
ALLOWED_HOSTS = ['{{ web_host }}']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

INSTANCE_NAME = '{{ web_host_name }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ db_name }}',
        'USER': '{{ db_user }}',
        'PASSWORD': '{{ db_password }}',
        'HOST': '{{ db_host }}',
        'PORT': '{{ db_port }}',
        'CONN_MAX_AGE': 300,
    }
}

# # Amazon S3
AWS_S3_HOST = '{{ aws_s3_host }}'

# Settings required for django-storages
AWS_STORAGE_BUCKET_NAME = '{{ aws_storage_bucket_name }}'
AWS_ACCESS_KEY_ID = None  # Set to None to use IAM role
AWS_SECRET_ACCESS_KEY = None  # Set to None to use IAM role

CORS_ORIGIN_WHITELIST = (
    '{{ web_host_name }}.aws.10clouds.com',
)

# If your Django app is behind a proxy that sets a header to specify secure
# connections, AND that proxy ensures that user-submitted headers with the
# same name are ignored (so that people can't spoof it), set this value to
# a tuple of (header_name, header_value). For any requests that come in with
# that header/value, request.is_secure() will return True.
# WARNING! Only set this if you fully understand what you're doing. Otherwise,
# you may be opening yourself up to a security risk.
# SECURE_PROXY_SSL_HEADER = ('HTTP_HTTPS', 'on')


# CORS_ORIGIN_ALLOW_ALL = True
