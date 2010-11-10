# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('django_page.views',
    (r'^(?P<url>.*)$', 'page'),
)
