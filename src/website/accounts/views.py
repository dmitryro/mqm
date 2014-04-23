# -*- coding: utf-8 -*-

from django.contrib.auth import login as auth_login
from django.contrib.auth.views import logout as auth_logout_view
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import is_safe_url

from .forms import LoginForm, SignupForm


def login_signup(request):
    if 'signup' in request.POST:
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect(reverse('signup-success'))
    else:
        signup_form = SignupForm()

    redirect_to = request.REQUEST.get('next', '')

    if 'login' in request.POST:
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = reverse('index')
            # Okay, security check complete. Log the user in.
            auth_login(request, login_form.get_user())
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            return HttpResponseRedirect(redirect_to)
    else:
        login_form = LoginForm()

    return render_to_response('registration/login.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    }, context_instance=RequestContext(request))


logout = auth_logout_view
