# -*- coding: utf-8 -*-
import os
import sys

PROJECT_ENVIRONMENT = 'dev'

IS_TESTING = False
for test_app in ['testserver','test']:
    if test_app in sys.argv[1:2]:
        IS_TESTING = True

SITE_ROOT = os.path.dirname(os.path.realpath(__file__+ '/../'))

DEBUG = True

ADMINS = (
    ("Ross Crawford-'dHeureuse", 'sendrossemail@gmail.com'),
)

MANAGERS = ADMINS + (
)


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mgmeckern_development',
        'USER': 'rosscdh',
        'PASSWORD': '',
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

gettext = lambda s: s

LANGUAGES = (
    ('de', gettext('German')),
    ('en', gettext('English')),
)

LOCALE_PATHS = (
    os.path.join(SITE_ROOT, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
# STATICFILES_DIRS = (
#     os.path.join(SITE_ROOT, '../', 'static'),
# )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sxtso-ceubz-6xq1hd!&p=q%9n4$9!e!$qk+m*8^z9_dfqg-j-'

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'mgmeckern.apps.public.context_processors.search_form',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'mgmeckern.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mgmeckern.wsgi.application'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.gis',
)

PROJECT_APPS = (
    'mgmeckern.apps.public',
    'mgmeckern.apps.report',
)

HELPER_APPS = (
    # 'south',
    'django_extensions',
    'crispy_forms',
    'parsley',
    'leaflet',
    'jsonify',
    'templatetag_handlebars',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'pipeline',
    'easy_thumbnails',
    'django_rq',
    'corsheaders',
)

INSTALLED_APPS = DJANGO_APPS + HELPER_APPS + PROJECT_APPS

if 'EMAIL_BACKEND' in os.environ and os.environ['EMAIL_BACKEND'] not in ['', None]:
    EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

USE_EMAIL_QUEUE = os.environ.get('USE_EMAIL_QUEUE', False)

#
# Templated Email
#
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'
TEMPLATED_EMAIL_TEMPLATE_DIR = 'email/'
TEMPLATED_EMAIL_FILE_EXTENSION = 'email'

if 'SENDGRID_USERNAME' in os.environ:
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://redistogo:49e729e96ed0a9d01796661836a54bf4@jack.redistogo.com:9735'),
        'DB': 0,
    }
}


PIPELINE = {}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        #'elbow.apps.api.permissions.ApiObjectPermission',
    ),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    # 'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 5,
}
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/tmp/mgmeckern-{env}.log'.format(env=PROJECT_ENVIRONMENT)
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'worker': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (51.19480, 6.42990),
    'DEFAULT_ZOOM': 17,
    'PLUGINS': {
        'GeoSearch': {
            'css': ['{STATIC_URL}css/l.geosearch.css'.format(STATIC_URL=STATIC_URL)],
            'js': ['{STATIC_URL}js/l.control.geosearch.js'.format(STATIC_URL=STATIC_URL), '{STATIC_URL}js/l.geosearch.provider.openstreetmap.js'.format(STATIC_URL=STATIC_URL)],
            'auto-include': True,
        },
    }
}

BASE_URL = 'http://localhost:8003'

# SOUTH_MIGRATION_MODULES = {
#     'easy_thumbnails': 'easy_thumbnails.south_migrations',
# }

# Neat trick http://www.robgolding.com/blog/2010/05/03/extending-settings-variables-with-local_settings-py-in-django/
try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        print("Could not load local_settings")

if IS_TESTING:
    try:
        from test_settings import *
    except ImportError:
        print("Could not load test_settings")
