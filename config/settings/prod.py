"""
Django project settings for the production environment.
"""
from .base import * # noqa

# NEED TO FIGURE OUT IF ZAPPA CERTIFY IS POSSIBLE HERE
ALLOWED_HOSTS = [

]

INSTALLED_APPS = INSTALLED_APPS + ['storages',]

# default django-storages settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_AUTO_CREATE_BUCKET = True

# S3 BUCKET STUFF GOES HERE
AWS_STATIC_BUCKET_NAME = 'rtk-static'
AWS_STATIC_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STATIC_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_STATIC_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'config.settings.storage_backends.StaticStorage'

# django-storages settings for all other files (including data files)
AWS_STORAGE_BUCKET_NAME = 'rtk-data'
AWS_DEFAULT_ACL = 'private'
AWS_BUCKET_ACL = 'private'

# Same idea as data location in local.py
DATA_LOCATION = 'rmp'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
