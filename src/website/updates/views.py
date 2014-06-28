# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from website.updates.models import Update, Openhub_Update
from website.views.generic import CommonPrivacyViewMixin



# National Mind Updates

class UpdateListView(ListView):
    queryset = Update.objects.order_by('-created')

update_list = UpdateListView.as_view()


class UpdateDetailView(DetailView):
    queryset = Update.objects.order_by('-created')

update_detail = UpdateDetailView.as_view()



# Openhub Updates

class Openhub_UpdateListView(ListView):
    queryset = Openhub_Update.objects.order_by('-created')

openhub_update_list = Openhub_UpdateListView.as_view()
