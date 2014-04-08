# -*- coding: utf-8 -*-
from contact_form.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required(login_url='/login/')
def app(request, path=None):
    return render_to_response('app.html', {
        'path': path,
    }, context_instance=RequestContext(request))
