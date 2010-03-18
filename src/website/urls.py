# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),

    url(r'^contact/$', 'contact', name='contact'),
    url(r'^about/$', 'about', name='about'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.views.generic.simple.direct_to_template', {'template': '403.html'}),
        url(r'^_404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        url(r'^_500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'', include('staticfiles.urls')),
    )
