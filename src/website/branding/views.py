from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView, TemplateView
from .models import Branding


class BrandingList(ListView):
    queryset = Branding.objects.all()

    def get_queryset(self):
        queryset = super(BrandingList, self).get_queryset()
        return queryset


branding_list = BrandingList.as_view()


class BrandingDetail(DetailView):
    template_name = 'branding/branding_detail.html'
    queryset = Branding.objects.all()


branding_detail = BrandingDetail.as_view()
