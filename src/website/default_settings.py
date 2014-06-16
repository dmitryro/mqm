# -*- coding: utf-8 -*-
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)))


def _project_config():
    from ConfigParser import SafeConfigParser
    config_file = os.path.join(PROJECT_ROOT, 'project.ini')
    project_config = SafeConfigParser()
    project_config.read(config_file)
    return project_config
project_config = _project_config()


PROJECT_NAME = project_config.get('project', 'name')
DOMAIN = project_config.get('project', 'domain')


###########################################################################
#                            project settings                             #
###########################################################################

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = (
    '%s' % DOMAIN,
    '%s.' % DOMAIN,
    'www.%s' % DOMAIN,
    'www.%s.' % DOMAIN,
    'localhost',
    '127.0.0.1',
)

# responsible persons
# -------------------

ADMINS = (
    (u'Angelo', u'angelo@ma-work.co.uk'),
    (u'Gregor', u'gregor@ma-work.co.uk'),
)
MANAGERS = ADMINS

# Email settings
# --------------

EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME
DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# i18n / l10n
# ------------

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en'
USE_I18N = True

DATE_FORMAT = 'F jS Y'

# more django core settings
# -------------------------

SITE_ID = 1

# Registration process settings
# -----------------------------

SIGNUP_TIMEOUT_DAYS = 1

# Media/Static file handling
# --------------------------

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'media', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Template related settings
# -------------------------

TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django_mobile.context_processors.flavour',
    'website.context_processors.site',
    'website.context_processors.api_keys',
)

INSTALLED_APPS = (
    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.formtools',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    # third-party apps
    'autofixture',
    'django_extensions',
    'django_markup',
    'django_mobile',
    'djangular',
    'contact_form',
    'flatblocks',
    'floppyforms',
    'rest_framework',
    #'haystack',
    'gunicorn',
    'mailer',
    'mediastore',
    'mediastore.mediatypes.download',
    'mediastore.mediatypes.embeded',
    'mediastore.mediatypes.image',
    'mediastore.mediatypes.pdf',
    'mediastore.mediatypes.video',
    'sorl.thumbnail',
    'sortedm2m',
    'taggit',
    'template_email',
    'tinymce',
    'south',

    # project apps
    'website',
    'website.accounts',
#    'website.alerts',
    'website.branding',
    'website.local_minds',
#    'website.clinical_research',
    'website.diary',
    'website.documents',
    'website.faq',
    'website.financial_summary',
    'website.funding_map',
    'website.growth',
    'website.local_map',
    'website.news',
    'website.pages',
    'website.privacy',
    'website.tasks',
    'website.resources',
    'website.services',
    'website.updates',
    'website.videos',
)

ROOT_URLCONF = 'website.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'website.pages.middleware.PageFallbackMiddleware',
)

AUTH_USER_MODEL = 'accounts.User'

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

###########################################################################
#                                 LOGGING                                 #
###########################################################################

LOGGING_DIR = os.path.join(PROJECT_ROOT, 'logs')

# create log directory if not exists yet
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file':{
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# global development options
# --------------------------

SKIP_SOUTH_TESTS = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


###########################################################################
#                            third-party apps                             #
###########################################################################

# TinyMCE
# -------

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'inlinepopups,safari',
    'theme': 'advanced',
    'theme_advanced_disable': 'underline,strikethrough,justifyleft,justifycenter,justifyright,justifyfull,numlist,outdent,indent,hr,styleselect,sub,sup',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'relative_urls': False,
    'dialog_type': 'modal',
    'entity_encoding': 'raw',
}

TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'

# haystack
# --------

HAYSTACK_SITECONF = 'website.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'search_index')

# rest-framework
# --------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}



##############################################################
#                          API KEYS                          #
##############################################################


GOOGLE_MAPS_API_KEY = None


###########################################################################
#                          local settings import                          #
###########################################################################

try:
    from local_settings import *
    if 'apply_settings' in globals():
        apply_settings(globals())
except ImportError:
    pass
