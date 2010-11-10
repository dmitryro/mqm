# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

DEFAULT_PAGE_APP = 'website.pages'

def get_page_app():
    """
    Get the page app (i.e. "django_page") as defined in the settings
    """
    # Make sure the app's in INSTALLED_APPS
    pages_app = get_page_app_name()
    if pages_app not in settings.INSTALLED_APPS:
        raise ImproperlyConfigured("The PAGE_APP (%r) "\
                                   "must be in INSTALLED_APPS" % settings.PAGE_APP)

    # Try to import the package
    try:
        package = import_module(pages_app)
    except ImportError:
        raise ImproperlyConfigured("The PAGE_APP setting refers to "\
                                   "a non-existing package.")
    return package

def get_page_app_name():
    """
    Returns the name of the page app (either the setting value, if it
    exists, or the default).
    """
    return getattr(settings, 'PAGE_APP', DEFAULT_PAGE_APP)

def get_model():
    """
    Returns the page model class.
    """
    if get_page_app_name() != DEFAULT_PAGE_APP and hasattr(get_page_app(), "get_model"):
        return get_page_app().get_model()
    else:
        from website.pages.models import Page
        return Page

def get_view():
    """
    Returns the page view.
    """
    if get_page_app_name() != DEFAULT_PAGE_APP and hasattr(get_page_app(), "get_view"):
        return get_page_app().get_view()
    else:
        from website.pages.views import page
        return page
