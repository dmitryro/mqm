# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site


def site(request):
    return {
        'site': Site.objects.get_current(),
    }


def api_keys(request):
    return {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
    }
