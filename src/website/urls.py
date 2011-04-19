# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),

    url(r'^contact/$', 'contact', name='contact'),
    url(r'^about/$', 'about', name='about'),
    
    url(r'^robots.txt$', direct_to_template, {'template': 'robots.txt'},),
    url(r'^humans.txt$', direct_to_template, {'template': 'humans.txt'},),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.views.generic.simple.direct_to_template', {'template': '403.html'}),
        url(r'^_404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        url(r'^_500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
    )
