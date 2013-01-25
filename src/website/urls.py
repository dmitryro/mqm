# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),

    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^about/$', 'website.views.about', name='about'),
    
    url(r'^robots.txt$', direct_to_template, {'template': 'robots.txt'},),
    url(r'^humans.txt$', direct_to_template, {'template': 'humans.txt'},),

    # mediastore download counter
    url(r'^downloads/(?P<slug>[^/]+)/download/(?P<filename>.+)$', 'mediastore.mediatypes.download.views.download_counter', name='mediastore-download-link'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.views.generic.simple.direct_to_template', {'template': '403.html'}),
        url(r'^_404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        url(r'^_500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
