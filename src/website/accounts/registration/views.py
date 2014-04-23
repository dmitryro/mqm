# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import base36_to_int

from ..models import ReservedEmail
from .tokens import token_generator


def signup_wizard(request, uidb36, token):
    try:
        uid_int = base36_to_int(uidb36)
        reserved = ReservedEmail.objects.get(pk=uid_int)
    except (ValueError, OverflowError, ReservedEmail.DoesNotExist):
        reserved = None

    if reserved is None or not token_generator.check_token(reserved, token):
        return invalid_url(request)

    # Wizard can be handled here.

    from django.http import HttpResponse
    return HttpResponse('Signup process here.')


def invalid_url(request):
    return render_to_response('registration/invalid_url.html', {
    }, context_instance=RequestContext(request))


def signup_confirmation(request):
    '''
    This view will be used after a user has successfully requested a
    registration link via the signup form.
    '''

    return render_to_response('registration/signup_confirmation.html', {
    }, context_instance=RequestContext(request))
