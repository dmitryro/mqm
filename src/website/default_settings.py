# -*- coding: utf-8 -*-
import os
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__)))


###########################################################################
#                            project settings                             #
###########################################################################

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# responsible persons
# -------------------

ADMINS = (
    (u'Angelo', u'angelo@ma-work.co.uk'),
    (u'Gregor', u'gregor@ma-work.co.uk'),
)
MANAGERS = ADMINS

# Email settings
# --------------

DEFAULT_FROM_EMAIL = 'angelo@ma-work.co.uk'

# i18n / l10n
# ------------

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en'
USE_I18N = True

# more django core settings
# -------------------------

SITE_ID = 1

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
    'compressor.finders.CompressorFinder',
)

# django-compressor
# -----------------

COMPRESS_JS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
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
)

INSTALLED_APPS = (
    # core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    # third-party apps
    'compressor',
    'django_extensions',
    'django_markup',
    'django_mobile',
    'contact_form',
    'flatblocks',
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
    'taggit',
    'tinymce',
    'south',

    # project apps
    'website',
    'website.pages',
)

ROOT_URLCONF = 'website.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'website.pages.middleware.PageFallbackMiddleware',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

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


###########################################################################
#                          local settings import                          #
###########################################################################

try:
    from local_settings import *
    if 'apply_settings' in globals():
        apply_settings(globals())
except ImportError:
    pass
