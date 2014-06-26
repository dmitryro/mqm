# -*- coding: utf-8 -*-
import floppyforms.__future__ as forms
from django.views.generic import DetailView
from website.views.generic import CommonPrivacyViewMixin, ListCreateView
from ..local_minds.models import LocalMind
from .forms import VideoForm
from .models import Video


class VideoListView(CommonPrivacyViewMixin, ListCreateView):
    form_class = VideoForm
    queryset = Video.objects.all()


video_list = VideoListView.as_view()


class VideoDetailView(CommonPrivacyViewMixin, DetailView):
    queryset = Video.objects.all()


video_detail = VideoDetailView.as_view()
