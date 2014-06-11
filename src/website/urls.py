# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^robots.txt$', 'django.shortcuts.render', {'template': 'robots.txt'},),
    url(r'^humans.txt$', 'django.shortcuts.render', {'template': 'humans.txt'},),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^signup/confirmation/$', 'website.accounts.registration.views.signup_confirmation', name='signup-confirmation'),
    url(r'^signup/(?P<uidb36>[^-/]+)-(?P<token>[^/]+)/$', 'website.accounts.registration.views.signup_wizard', name='signup'),
    url(r'^signup/(?P<uidb36>[^-/]+)-(?P<token>[^/]+)/(?P<step>[^/]+)/$', 'website.accounts.registration.views.signup_wizard', name='signup'),
    url(r'^api/', include('website.api.urls')),

    #ANGELO Generic Views
    url(r'^stream/$', 'website.videos.views.video_list', name='videos'),
    url(r'^stream/(?P<pk>\d+)/$', 'website.videos.views.video_detail', name='videos'),
    url(r'^branding/$', 'website.branding.views.branding_list', name='branding'),
    url(r'^branding/(?P<pk>\d+)/$', 'website.branding.views.branding_detail', name='branding'),
    url(r'^diary/$', 'website.diary.views.event_list', name='event'),
    url(r'^document/$', 'website.documents.views.document_list', name='document'),
    url(r'^document/\+(?P<category_slug>[^/]+)/$', 'website.documents.views.document_list', name='document'),
    url(r'^document/(?P<slug>[^/]+)/$', 'website.documents.views.document_detail', name='document'),


    url(r'^login/$', 'website.accounts.views.login_signup', name='login'),
    url(r'^login/$', 'website.accounts.views.login_signup', name='signup'),
    url(r'^logout/$', 'website.accounts.views.logout', name='logout'),

    # mediastore download counter
    url(r'^downloads/(?P<slug>[^/]+)/download/(?P<filename>.+)$', 'mediastore.mediatypes.download.views.download_counter', name='mediastore-download-link'),

    url(r'^admin/', include(admin.site.urls)),


    #static design templates
    url(r'^my-dashboard/$', 'django.shortcuts.render', {'template_name': 'dev/dashboard.html'}),
    url(r'^local-dashboard/$', 'django.shortcuts.render', {'template_name': 'dev/local-dashboard.html'}),
    url(r'^video-stream/$', 'django.shortcuts.render', {'template_name': 'dev/video.html'}),
    url(r'^meet-the-team/$', 'django.shortcuts.render', {'template_name': 'dev/meet-the-team.html'}),
    url(r'^meet-the-team-member/$', 'django.shortcuts.render', {'template_name': 'dev/team.html'}),
    url(r'^local-mind/$', 'django.shortcuts.render', {'template_name': 'dev/lm.html'}),
    url(r'^events-diary/$', 'django.shortcuts.render', {'template_name': 'dev/event-diary.html'}),
    url(r'^my-local-area/$', 'django.shortcuts.render', {'template_name': 'dev/local-map.html'}),
    url(r'^funding-map/$', 'django.shortcuts.render', {'template_name': 'dev/funding-map.html'}),
    url(r'^todos/$', 'django.shortcuts.render', {'template_name': 'dev/task.html'}),
    url(r'^call-out/$', 'django.shortcuts.render', {'template_name': 'dev/questions-and-answers.html'}),
    url(r'^engine-room/$', 'django.shortcuts.render', {'template_name': 'dev/documents.html'}),
    url(r'^external-news/$', 'django.shortcuts.render', {'template_name': 'dev/external-news.html'}),
    url(r'^positive-news/$', 'django.shortcuts.render', {'template_name': 'dev/positive-news.html'}),

    url(r'^sign-up/part1$', 'django.shortcuts.render', {'template_name': 'dev/signup/part1.html'}),
    url(r'^sign-up/part2$', 'django.shortcuts.render', {'template_name': 'dev/signup/part2.html'}),
    url(r'^sign-up/part3$', 'django.shortcuts.render', {'template_name': 'dev/signup/part3.html'}),
    url(r'^sign-up/part4$', 'django.shortcuts.render', {'template_name': 'dev/signup/part4.html'}),
    url(r'^sign-up/part5$', 'django.shortcuts.render', {'template_name': 'dev/signup/part5.html'}),
    url(r'^sign-up/part6$', 'django.shortcuts.render', {'template_name': 'dev/signup/part6.html'}),

    #modals
    #url(r'^_addClinicalResearch/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-clinical-research.html'}),
    #url(r'^_addExternalNews/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-external-news.html'}),
    url(r'^_addPositiveNews/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-positive-news.html'}),
    url(r'^_addService/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-service.html'}),
    url(r'^_addEvent/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-event.html'}),
    url(r'^_addKeyPartner/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-key-partner.html'}),
    url(r'^_addFunding/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-funding.html'}),
    url(r'^_addTodo/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-todo.html'}),
    url(r'^_addQuestion/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-question.html'}),
    url(r'^_addDocument/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-document.html'}),
    url(r'^_addNews/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-news.html'}),
    url(r'^_addVideo/$', 'django.shortcuts.render', {'template_name': 'dev/modals/add-video.html'}),


    #general
     url(r'^log-in/$', 'django.shortcuts.render', {'template_name': 'dev/login.html'}),
     url(r'^invitee/$', 'django.shortcuts.render', {'template_name': 'dev/invitee.html'})
)

app_patterns = patterns('',
    url(r'^$', 'website.views.app', name='app'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^_403/$', 'django.shortcuts.render', {'template_name': '403.html'}),
        url(r'^_404/$', 'django.shortcuts.render', {'template_name': '404.html'}),
        url(r'^_500/$', 'django.shortcuts.render', {'template_name': '500.html'}),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += app_patterns
