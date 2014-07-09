# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='/login/')
def app(request, path=None):
    return render_to_response('app.html', {
        'path': path,
    }, context_instance=RequestContext(request))
