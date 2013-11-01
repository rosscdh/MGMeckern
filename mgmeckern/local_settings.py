# -*- coding: utf-8 -*-
LOCAL_SETTINGS = True
from settings import *

import dj_database_url

PROJECT_ENVIRONMENT = 'preview'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# extract url from env variable
DATABASES['default'] = dj_database_url.config()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'app19086916@heroku.com'
EMAIL_HOST_PASSWORD = 'eoznj7ol'
DEFAULT_FROM_EMAIL = 'no-reply@mgm.herokuapp.com'
SERVER_EMAIL = 'no-reply@mgm.herokuapp.com'