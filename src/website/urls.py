# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.index', name='index'),

    url(r'^contact/$', 'website.views.contact', name='contact'),
    url(r'^about/$', 'website.views.about', name='about'),
    
    url(r'^robots.txt$', 'django.shortcuts.render', {'template': 'robots.txt'},),
    url(r'^humans.txt$', 'django.shortcuts.render', {'template': 'humans.txt'},),

    # mediastore download counter
    url(r'^downloads/(?P<slug>[^/]+)/download/(?P<filename>.+)$', 'mediastore.mediatypes.download.views.download_counter', name='mediastore-download-link'),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.shortcuts.render', {'template_name': '403.html'}),
        url(r'^_404/$', 'django.shortcuts.render', {'template_name': '404.html'}),
        url(r'^_500/$', 'django.shortcuts.render', {'template_name': '500.html'}),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
