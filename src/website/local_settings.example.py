# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))

###########
# DATABSE #
###########

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': os.path.join(path, '../../db.sqlite'),
    }
}

#########
# EMAIL #
#########

ADMINS = (
    ('Angelo', 'angelo@ma-work.co.uk'),
    ('Gregor', 'gregor@ma-work.co.uk'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'

# remove this in production
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

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

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#COMPRESS = True
