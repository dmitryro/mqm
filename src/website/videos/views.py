from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from .models import Video


class VideoList(ListView):
    queryset = Video.objects.all()

    def get_queryset(self):
        queryset = super(VideoList, self).get_queryset()
        return queryset


video_list = VideoList.as_view()


class VideoDetail(DetailView):
    template_name = 'videos/video_detail.html'
    queryset = Video.objects.all()


video_detail = VideoDetail.as_view()
