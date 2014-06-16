# -*- coding: utf-8 -*-
from django.views.generic import ListView
from website.views.generic import CommonPrivacyViewMixin
from ..local_minds.models import LocalMind
from .models import Resource


class ResourceListView(CommonPrivacyViewMixin, ListView):
    queryset = Resource.objects.all()

    def get_context_data(self, **kwargs):
        resources_by_lm_pks = {}
        for resource in self.object_list.all():
            resources_by_lm_pks.setdefault(resource.local_mind_id, []).append(resource)
        local_minds_by_pk = dict(
            (local_mind.pk, local_mind)
            for local_mind in LocalMind.objects.filter(pk__in=resources_by_lm_pks.keys()))
        kwargs['local_minds_with_resources'] = list(
            (local_minds_by_pk[key], value)
            for key, value in resources_by_lm_pks.items())
        return super(ResourceListView, self).get_context_data(**kwargs)


resource_list = ResourceListView.as_view()
