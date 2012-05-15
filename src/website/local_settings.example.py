# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))

###########
# DATABSE #
###########

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': '<REPLACE:PROJECT_NAME>',
#        'USER': '<REPLACE:PROJECT_NAME>',
#        'PASSWORD': '<REPLACE:MYSQL_PASSWORD>',
#    }
#}

#########
# EMAIL #
#########

ADMINS = (
    ('Angelo', 'angelo@ma-work.co.uk'),
    ('Gregor', 'gregor@ma-work.co.uk'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'

INTERNAL_IPS = ('127.0.0.1',)

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

#########
# MEDIA #
#########

#MEDIA_URL = 'http://media.<REPLACE:DOMAIN>/'

#STATIC_URL = 'http://static.<REPLACE:DOMAIN>/'
#COMPRESS_URL = STATIC_URL

##############
# SECRET KEY #
##############

# Make this unique, and don't share it with anybody.
SECRET_KEY = '<REPLACE:SECRET_KEY>'

##########################
# DEVELOPMENT OVERWRITES #
##########################

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(path, '../../db.sqlite'),
    }
}

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#COMPRESS = True
