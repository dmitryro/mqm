import calendar
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.encoding import force_str

from website.views.generic import CommonPrivacyViewMixin
from ..local_minds.models import LocalMind
from .models import Event


class EventList(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.all()

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()
        return queryset


event_list = EventList.as_view()


class EventDetail(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.all()


event_detail = EventDetail.as_view()


class EventAPIList(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.select_related('local_mind', 'user')

    def get_queryset(self):
        queryset = super(EventAPIList, self).get_queryset()
        return queryset

    def serialize_datetime(self, datetime):
        return calendar.timegm(datetime.timetuple()) * 1000

    def serialize_object(self, obj):
        return {
            'id': obj.pk,
            'user': {
                'id': obj.user.pk,
                'name': obj.user.get_full_name(),
            },
            'local_mind': {
                'id': obj.local_mind.pk,
                'name': obj.local_mind.name,
                'region': obj.local_mind.region,
            },
            'title': obj.title,
            'url': obj.get_absolute_url(),
            'class': 'event-important',
            'start': self.serialize_datetime(obj.start),
            'end': self.serialize_datetime(obj.end),
        }

    def serialize_object_list(self, object_list):
        regions = dict(
            (
                force_str(slug),
                force_str(name),
            ) for slug, name in LocalMind.REGION_CHOICES)
        return {
            'success': 1,
            'result': [self.serialize_object(obj) for obj in object_list],
            'regions': regions,
        }

    def filter_queryset(self, queryset):
        limit = self.kwargs['limit']
        if limit == 'own':
            queryset = queryset.filter(user=self.request.user)
        elif limit == 'local':
            queryset = queryset.filter(local_mind=self.request.user.local_mind)
        elif limit == 'national':
            pass
        else:
            raise AssertionError('Did not get expected value for "limit".')

        regions = self.request.GET.getlist('region')
        if regions:
            queryset = queryset.filter(local_mind__region__in=regions)
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        data = self.serialize_object_list(queryset)
        return HttpResponse(
            json.dumps(data),
            content_type='application/json')


event_api_list = EventAPIList.as_view()
