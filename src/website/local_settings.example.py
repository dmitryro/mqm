# -*- coding: utf-8 -*-
from default_settings import *

import os
path = os.path.abspath(os.path.dirname(__file__))


#DEBUG = True
TEMPLATE_DEBUG = DEBUG


###########################################################################
#                            database settings                            #
###########################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '%(PROJECT_NAME)s',
        'USER': '%(PROJECT_NAME)s',
        'PASSWORD': '%(MYSQL_PASSWORD)s',
    }
}


###########################################################################
#                             email settings                              #
###########################################################################

DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'

# GMail Email setup
# -----------------

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(PROJECT_ROOT, 'logs/emails/')

# SES Email setup
# ---------------

#EMAIL_BACKEND = 'django_ses.SESBackend'
#AWS_ACCESS_KEY_ID = ''
#AWS_SECRET_ACCESS_KEY = ''


###########################################################################
#                        media / static files urls                        #
###########################################################################

MEDIA_URL = 'http://media.%(DOMAIN)s/'

STATIC_URL = 'http://static.%(DOMAIN)s/'
COMPRESS_URL = STATIC_URL


###########################################################################
#                              secret sauce                               #
###########################################################################

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%(SECRET_KEY)s'
