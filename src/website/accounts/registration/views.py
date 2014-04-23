# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def signup_wizard(request, token):
    from django.http import HttpResponse
    return HttpResponse('Signup process here.')


def signup_confirmation(request):
    return render_to_response('registration/signup_confirmation.html', {
    }, context_instance=RequestContext(request))
