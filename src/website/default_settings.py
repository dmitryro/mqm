# -*- coding: utf-8 -*-
import os
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_ACCESS_KEY_ID = 'defined in local_settings.py'
AWS_SECRET_ACCESS_KEY = 'defined in local_settings.py'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

STATICFILES_EXCLUDED_APPS = (
    'debug_toolbar',
)

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = '_cache'

COMPRESS_CSS_FILTERS = [
    'compressor_cssmin.CSSMinFilter',
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'defined in local_settings.py'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'staticfiles.context_processors.static_url',
    'django_mobile.context_processors.flavour',
    'website.context_processors.site',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'website.pages.middleware.PageFallbackMiddleware',
)

ROOT_URLCONF = 'website.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    # load patches first
    'website.patch',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.webdesign',
    'django_extensions',
    'django_markup',
    'django_mobile',
    'compressor',
    'contact_form',
    'debug_toolbar',
    'flatblocks',
    'gunicorn',
    'mailer',
    'mediastore',
    'mediastore.mediatypes.download',
    'mediastore.mediatypes.embeded',
    'mediastore.mediatypes.image',
    'mediastore.mediatypes.pdf',
    'mediastore.mediatypes.video',
    'sorl.thumbnail',
    'staticfiles',
    'tagging',
    'tinymce',

    'website',
    'website.pages',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

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

LOGIN_REDIRECT_URL = '/'

SKIP_SOUTH_TESTS = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


try:
    from local_settings import *
    if 'apply_settings' in globals():
        apply_settings(globals())
except ImportError:
    pass
