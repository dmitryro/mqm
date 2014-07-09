import calendar
from datetime import date, timedelta
import json

from django.http import HttpResponse
from django.views.generic import ListView

from website.views.generic import CommonPrivacyViewMixin, ListCreateView
from ..local_minds.models import LocalMind
from .forms import EventForm
from .models import Event


class EventCalendar(CommonPrivacyViewMixin, ListCreateView):
    queryset = Event.objects.all()
    form_class = EventForm
    template_name = 'diary/event_calendar.html'

    def get_context_data(self, **kwargs):
        context = super(EventCalendar, self).get_context_data(**kwargs)
        context['regions'] = LocalMind.REGION_CHOICES
        return context


event_calendar = EventCalendar.as_view()


class EventDetail(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.all()


event_detail = EventDetail.as_view()


class EventAPIList(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.select_related('local_mind', 'user')

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
            'privacy': obj.privacy,
        }

    def serialize_object_list(self, object_list):
        return {
            'success': 1,
            'result': [self.serialize_object(obj) for obj in object_list],
        }

    def filter_queryset(self, queryset):
        regions = self.request.GET.getlist('region')
        if regions:
            queryset = queryset.filter(local_mind__region__in=regions)

        limit = self.kwargs['limit']
        if limit == 'own':
            queryset = queryset.filter(user=self.request.user)
        elif limit == 'local':
            queryset = queryset.filter(local_mind=self.request.user.local_mind)
        elif limit == 'national':
            # Return no events when no region is given.
            if not regions:
                queryset = queryset.none()
        else:
            raise AssertionError('Did not get expected value for "limit".')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        data = self.serialize_object_list(queryset)
        return HttpResponse(
            json.dumps(data),
            content_type='application/json')


event_api_list = EventAPIList.as_view()


class EventAPICurrentDates(CommonPrivacyViewMixin, ListView):
    queryset = Event.objects.all()

    def filter_queryset(self, queryset):
        today = date.today()
        month_start = today.replace(day=1)
        month_end = (month_start + timedelta(days=31)).replace(day=1) - timedelta(days=1)
        queryset = queryset.filter(start__range=(month_start, month_end))
        return queryset

    def serialize_object(self, obj):
        return '{day}-{month}-{year}'.format(
            day=obj.day,
            month=obj.month,
            year=obj.year)

    def serialize_object_list(self, object_list):
        return [
            self.serialize_object(obj) for obj in object_list
        ]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        queryset = queryset.dates('start', kind='day')
        data = self.serialize_object_list(queryset)
        return HttpResponse(
            json.dumps(data),
            content_type='application/json')


event_api_current_dates = EventAPICurrentDates.as_view()
