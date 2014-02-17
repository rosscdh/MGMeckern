# -*- coding: utf-8 -*-
LOCAL_SETTINGS = True
from settings import *

PROJECT_ENVIRONMENT = 'staging'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/m/mgm/media/'
STATIC_URL = '/s/mgm/static/'

MEDIA_ROOT = '/home/rosscdh/webapps/htdocs/mgm/media/'
STATICFILES_DIRS = (
    '/home/rosscdh/webapps/htdocs/mgm/static/',
)