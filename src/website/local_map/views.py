# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.local_minds.models import LocalMind
from website.views.generic import CommonPrivacyViewMixin, ListCreateView
from .forms import MapForm
from .models import Map


class MapListView(CommonPrivacyViewMixin, ListCreateView):
    form_class = MapForm
    queryset = Map.objects.exclude(_latitude_postcode=None, _longitude_postcode=None)

    def get_form_kwargs(self):
        kwargs = super(MapListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['model'] = self.queryset.model
        #local_minds = LocalMind.objects.exclude(pk=self.request.user.local_mind.pk)
        #local_minds = local_minds.exclude(_latitude_postcode=None, _longitude_postcode=None)
        kwargs['local_minds'] = local_minds
        return super(MapListView, self).get_context_data(**kwargs)


map_list = MapListView.as_view()
