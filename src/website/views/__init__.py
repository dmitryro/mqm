# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', {
    }, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def app(request, path=None):
    return render_to_response('app.html', {
        'path': path,
    }, context_instance=RequestContext(request))
