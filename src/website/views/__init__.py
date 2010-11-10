# -*- coding: utf-8 -*-
from contact_form.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', {
    }, context_instance=RequestContext(request))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('%s?success' % request.path)
    else:
        form = ContactForm(request=request)
    return render_to_response('contact_form/contact_form.html', {
        'form': form,
        'success': 'success' in request.GET,
    }, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {
    }, context_instance=RequestContext(request))
