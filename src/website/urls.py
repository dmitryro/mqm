# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import RedirectView

admin.autodiscover()


def protected_render(request, *args, **kwargs):
    valid_request = False
    if request.user.is_authenticated():
        valid_request = True
    if not valid_request:
        raise Http404
    return render(request, *args, **kwargs)


development_urlpatterns = patterns('',

    # Development static design templates
    url(r'^d/my-dashboard/$', protected_render, {'template_name': 'dev/dashboard.html'}),
    url(r'^d/local-dashboard/$', protected_render, {'template_name': 'dev/local-dashboard.html'}),
    url(r'^d/video-stream/$', protected_render, {'template_name': 'dev/video.html'}),
    url(r'^d/meet-the-team/$', protected_render, {'template_name': 'dev/meet-the-team.html'}),
    url(r'^d/meet-the-team-member/$', protected_render, {'template_name': 'dev/team.html'}),
    url(r'^d/local-mind/$', protected_render, {'template_name': 'dev/lm.html'}),
    url(r'^d/events-diary/$', protected_render, {'template_name': 'dev/event-diary.html'}),
    url(r'^d/my-local-area/$', protected_render, {'template_name': 'dev/local-map.html'}),
    url(r'^d/funding-map/$', protected_render, {'template_name': 'dev/funding-map.html'}),
    url(r'^d/todos/$', protected_render, {'template_name': 'dev/task.html'}),
    url(r'^d/call-out/$', protected_render, {'template_name': 'dev/questions-and-answers.html'}),
    url(r'^d/engine-room/$', protected_render, {'template_name': 'dev/documents.html'}),
    url(r'^d/external-news/$', protected_render, {'template_name': 'dev/external-news.html'}),
    url(r'^d/positive-news/$', protected_render, {'template_name': 'dev/positive-news.html'}),
    url(r'^d/brand/$', protected_render, {'template_name': 'dev/brand.html'}),
    url(r'^d/the-net-works/$', protected_render, {'template_name': 'dev/the-net-works.html'}),
    url(r'^d/openhub-updates/$', protected_render, {'template_name': 'dev/openhub-updates.html'}),
    url(r'^d/national-mind-updates/$', protected_render, {'template_name': 'dev/national-mind-updates.html'}),
    url(r'^d/buddy-search/$', protected_render, {'template_name': 'dev/buddy-search.html'}),
    url(r'^d/hot-topic-news/$', protected_render, {'template_name': 'dev/hot-topic-news.html'}),
    url(r'^d/engine-room-2/$', protected_render, {'template_name': 'dev/engine-room.html'}),


    url(r'^sign-up/part1$', protected_render, {'template_name': 'dev/signup/part1.html'}),
    url(r'^sign-up/part2$', protected_render, {'template_name': 'dev/signup/part2.html'}),
    url(r'^sign-up/part3$', protected_render, {'template_name': 'dev/signup/part3.html'}),
    url(r'^sign-up/part4$', protected_render, {'template_name': 'dev/signup/part4.html'}),
    url(r'^sign-up/part5$', protected_render, {'template_name': 'dev/signup/part5.html'}),
    url(r'^sign-up/part6$', protected_render, {'template_name': 'dev/signup/part6.html'}),

    #modals
    #url(r'^_addClinicalResearch/$', protected_render, {'template_name': 'dev/modals/add-clinical-research.html'}),
    #url(r'^_addExternalNews/$', protected_render, {'template_name': 'dev/modals/add-external-news.html'}),
    url(r'^_addPositiveNews/$', protected_render, {'template_name': 'dev/modals/add-positive-news.html'}),
    url(r'^_addService/$', protected_render, {'template_name': 'dev/modals/add-service.html'}),
    url(r'^_addEvent/$', protected_render, {'template_name': 'dev/modals/add-event.html'}),
    url(r'^_addKeyPartner/$', protected_render, {'template_name': 'dev/modals/add-key-partner.html'}),
    url(r'^_addFunding/$', protected_render, {'template_name': 'dev/modals/add-funding.html'}),
    url(r'^_addTodo/$', protected_render, {'template_name': 'dev/modals/add-todo.html'}),
    url(r'^_addQuestion/$', protected_render, {'template_name': 'dev/modals/add-question.html'}),
    url(r'^_addDocument/$', protected_render, {'template_name': 'dev/modals/add-document.html'}),
    url(r'^_addNews/$', protected_render, {'template_name': 'dev/modals/add-news.html'}),
    url(r'^_addVideo/$', protected_render, {'template_name': 'dev/modals/add-video.html'}),
    url(r'^_addPassword/$', protected_render, {'template_name': 'dev/modals/change-password.html'}),
    url(r'^_addResource/$', protected_render, {'template_name': 'dev/modals/add-resource.html'}),
    url(r'^_addAnswer/$', protected_render, {'template_name': 'dev/modals/add-answer.html'}),


    #calendar widget urls
    url(r'^calendarTemplates/day.html$', protected_render, {'template_name': 'calendarTemplates/day.html'}),
    url(r'^calendarTemplates/events-list.html$', protected_render, {'template_name': 'calendarTemplates/events-list.html'}),
    url(r'^calendarTemplates/modal.html$', protected_render, {'template_name': 'calendarTemplates/modal.html'}),
    url(r'^calendarTemplates/month-day.html$', protected_render, {'template_name': 'calendarTemplates/month-day.html'}),
    url(r'^calendarTemplates/month.html$', protected_render, {'template_name': 'calendarTemplates/month.html'}),
    url(r'^calendarTemplates/week-days.html$', protected_render, {'template_name': 'calendarTemplates/week-days.html'}),
    url(r'^calendarTemplates/week.html$', protected_render, {'template_name': 'calendarTemplates/week.html'}),
    url(r'^calendarTemplates/year-month.html$', protected_render, {'template_name': 'calendarTemplates/year-month.html'}),
    url(r'^calendarTemplates/year.html$', protected_render, {'template_name': 'calendarTemplates/year.html'}),
    #

    #general
     url(r'^log-in/$', protected_render, {'template_name': 'dev/login.html'}),
     url(r'^invitee/$', protected_render, {'template_name': 'dev/invitee.html'})
)

urlpatterns = patterns('',
    url(r'^robots.txt$', 'django.shortcuts.render', {'template': 'robots.txt'},),
    url(r'^humans.txt$', 'django.shortcuts.render', {'template': 'humans.txt'},),

    url(r'^api/events/(?P<limit>own|local|national)/$', 'website.diary.views.event_api_list', name='api-events'),
    url(r'^api/events/$', 'website.diary.views.event_api_list', name='api-events'),

    #url(r'^$', 'website.views.index', name='index'),
    url(r'^$', RedirectView.as_view(url='/login/')),
    url(r'^signup/profile/(?P<uidb36>[^-/]+)-(?P<token>[^/]+)/$', 'website.accounts.registration.views.signup_profile', name='signup-profile'),
    url(r'^signup/(?P<uidb36>[^-/]+)-(?P<token>[^/]+)/$', 'website.accounts.registration.views.signup_wizard', name='signup'),
    url(r'^signup/(?P<uidb36>[^-/]+)-(?P<token>[^/]+)/(?P<step>[^/]+)/$', 'website.accounts.registration.views.signup_wizard', name='signup'),
    url(r'^api/', include('website.api.urls')),

    # PRODUCTION ready for Workshop 1 -- GREGOR TO COMPLETE THESE
    url(r'^my-dashboard/$', 'website.accounts.dashboard.views.dashboard', name='dashboard'),
    url(r'^my-dashboard/local-mind/$', 'website.accounts.dashboard.views.local_mind_form', name='local-mind-form'),
    url(r'^my-dashboard/profile/$', 'website.accounts.dashboard.views.profile_form', name='profile-form'),
    url(r'^my-dashboard/invite/$', 'website.accounts.dashboard.views.invite_form', name='invite-form'),
    url(r'^my-dashboard/change-password/$', 'website.accounts.dashboard.views.change_password', name='change-password'),
    url(r'^my-local-area/$', 'website.local_map.views.map_list', name='local-map'),
    url(r'^my-local-area/add/$', 'website.local_map.views.map_list', {'show_form': True}, name='local-map-add'),
    url(r'^positive-news/$', 'website.news.views.positive_news_list', name='positive-news'),
    url(r'^positive-news/add/$', 'website.news.views.positive_news_list', {'show_form': True},  name='positive-news-add'),
    url(r'^positive-news/(?P<slug>[^/]+)/$', 'website.news.views.positive_news_detail', name='positive-news'),

    # ANGELO
    url(r'^external-news/$', 'website.news.views.external_news_list', name='external-news'),
    url(r'^external-news/(?P<slug>[^/]+)/$', 'website.news.views.external_news_detail', name='external-news'),
    url(r'^mind-updates/$', 'website.updates.views.update_list', name='mind-updates'),
    url(r'^mind-updates/(?P<slug>[^/]+)/$', 'website.updates.views.update_detail', name='mind-updates'),
    url(r'^openhub-updates/$', 'website.updates.views.openhub_update_list', name='hub-updates'),
    #url(r'^hub-updates/(?P<slug>[^/]+)/$', 'website.updates.views.openhub_update_detail', name='hub-updates'),

    url(r'^call-out/$', 'website.faq.views.question_list', name='questions'),
    url(r'^call-out/add/$', 'website.faq.views.question_list', {'show_form': True}, name='questions'),
    url(r'^call-out/(?P<pk>\d+)/$', 'website.faq.views.question_detail', name='questions'),
    url(r'^call-out/(?P<pk>\d+)/add-answer/$', 'website.faq.views.question_detail', {'show_form': True}, name='questions-add-answer'),
    url(r'^meet-the-team/$', 'website.local_minds.views.team_detail', name='team'),
    url(r'^meet-the-team/(?P<slug>[^/]+)/$', 'website.local_minds.views.team_detail', name='team'),
    url(r'^meet-the-team/(?P<local_mind_slug>[^/]+)/(?P<slug>[^/]+)/$', 'website.local_minds.views.user_detail', {'template_name': 'dev/team.html'}, name='team'),
    url(r'^local-mind/(?P<slug>[^/]+)/$', 'website.local_minds.views.local_mind_detail', name='local-mind'),
    url(r'^todos/$', 'website.tasks.views.task_list', name='tasks'),
    url(r'^todos/add/$', 'website.tasks.views.task_list', {'show_form': True}, name='tasks-add'),
    url(r'^todos/(?P<pk>\d+)/done/$', 'website.tasks.views.task_done', {'done': True}, name='tasks-done'),
    url(r'^todos/(?P<pk>\d+)/undone/$', 'website.tasks.views.task_done', {'done': False}, name='tasks-undone'),
    url(r'^the-net-works/$', 'website.resources.views.resource_list', name='net-works'),
    url(r'^diary-events/$', 'website.diary.views.event_calendar', name='events'),
    url(r'^diary-events/(?P<slug>[^/]+)/$', 'website.diary.views.event_detail', name='events'),
    url(r'^funding-map/$', 'website.funding_map.views.funding_list', name='fundings'),
    url(r'^video-stream/$', 'website.videos.views.video_list', name='videos'),
    url(r'^video-stream/(?P<slug>[^/]+)/$', 'website.videos.views.video_detail', name='videos'),
    url(r'^engine-room/$', 'website.documents.views.category_list', name='documents-categories'),
    url(r'^engine-room/documents/$', 'website.documents.views.document_list', name='documents'),
    url(r'^engine-room/documents/(?P<slug>[^/]+)/$', 'website.documents.views.document_detail', name='documents'),

    url(r'^login/$', 'website.accounts.views.login_signup', name='login'),
    url(r'^login/signup/$', lambda r: HttpResponseRedirect(reverse('login') + '#signup'), name='signup'),
    url(r'^signup/confirmation/$', 'website.accounts.views.signup_confirmation', name='signup-confirmation'),
    url(r'^logout/$', 'website.accounts.views.logout', name='logout'),
    url(r'^forgot/$', 'website.accounts.views.password_reset', name='password-reset'),
    url(r'^forgot/done/$', 'website.accounts.views.password_reset_done', name='password-reset-done'),
    url(r'^forgot/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'website.accounts.views.password_reset_confirm', name='password-reset-confirm'),
    url(r'^forgot/complete/$', 'website.accounts.views.password_reset_complete', name='password-reset-complete'),

    # mediastore download counter
    url(r'^downloads/(?P<slug>[^/]+)/download/(?P<filename>.+)$', 'mediastore.mediatypes.download.views.download_counter', name='mediastore-download-link'),

    url(r'^admin/', include(admin.site.urls)),

    # Developemnt Basic Views
    #url(r'^stream/$', 'website.videos.views.video_list', name='videos'),
    #url(r'^stream/(?P<pk>\d+)/$', 'website.videos.views.video_detail', name='videos'),
    #url(r'^branding/$', 'website.branding.views.branding_list', name='branding'),
    #url(r'^branding/(?P<pk>\d+)/$', 'website.branding.views.branding_detail', name='branding'),
    #url(r'^diary/$', 'website.diary.views.event_list', name='event'),
    #url(r'^document/$', 'website.documents.views.document_list', name='document'),
    #url(r'^document/\+(?P<category_slug>[^/]+)/$', 'website.documents.views.document_list', name='document'),
    #url(r'^document/(?P<slug>[^/]+)/$', 'website.documents.views.document_detail', name='document'),

    url(r'^', include(development_urlpatterns)),
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
