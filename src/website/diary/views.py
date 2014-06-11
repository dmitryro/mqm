from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from .models import Event


class EventList(ListView):
    queryset = Event.objects.all()

    def get_queryset(self):
        queryset = super(EventList, self).get_queryset()
        return queryset


event_list = EventList.as_view()
