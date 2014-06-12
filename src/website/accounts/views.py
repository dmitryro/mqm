# -*- coding: utf-8 -*-

from django.contrib.auth import login as auth_login
import django.contrib.auth.views as auth_views
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import is_safe_url

from .forms import LoginForm, SignupForm, PasswordResetForm


LOGIN_SUCCESS_URLNAME = 'dashboard'


def login_signup(request):
    if 'signup' in request.POST:
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponseRedirect(reverse('signup-confirmation'))
    else:
        signup_form = SignupForm()

    redirect_to = request.REQUEST.get('next', '')

    if 'login' in request.POST:
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = reverse(LOGIN_SUCCESS_URLNAME)
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


def signup_confirmation(request):
    return render_to_response('registration/signup_confirmation.html', {
    }, context_instance=RequestContext(request))


logout = auth_views.logout


def password_reset(request):
    return auth_views.password_reset(
        request,
        password_reset_form=PasswordResetForm,
        post_reset_redirect=reverse('password-reset-done'))


password_reset_done = auth_views.password_reset_done


def password_reset_confirm(request, uidb36, token):
    return auth_views.password_reset_confirm(
        request,
        uidb36=uidb36,
        token=token,
        post_reset_redirect=reverse('password-reset-complete'))


password_reset_complete = auth_views.password_reset_complete
