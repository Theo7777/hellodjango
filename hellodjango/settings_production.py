#settings_production.py

from settings import *

DEBUG = TEMPLATE_DEBUG = False

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://roundworld.s3.amazonaws.com/static/'