# -*- coding: utf-8 -*-
LOCAL_SETTINGS = True
from settings import *

PROJECT_ENVIRONMENT = 'staging'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/rosscdh/webapps/htdocs/mgm/media'
STATIC_ROOT = '/home/rosscdh/webapps/htdocs/mgm/static'

STATICFILES_DIRS = ()

     = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '/home/rosscdh/webapps/mgm/dev.db',
}

DATABASES = {
    'default': db_config
}