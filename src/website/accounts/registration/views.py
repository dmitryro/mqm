# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.contrib import auth
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.utils.http import base36_to_int
from django.views.generic import FormView

from ..models import User, ReservedEmail
from .tokens import token_generator
from .forms import SignupLocalMindForm, SignupProfileForm, SignupLocalMindMembersForm, SignupPartnersForm, SignupInviteForm
from .forms import SignupUserProfileForm


class SignupLogicMixin(object):
    def get_token_object(self, uid_int):
        raise NotImplementedError()

    def check_token(self):
        uidb36 = self.kwargs['uidb36']
        token = self.kwargs['token']

        try:
            uid_int = base36_to_int(uidb36)
            obj = self.get_token_object(uid_int)
        except (ValueError, OverflowError):
            obj = None

        if obj is None or not token_generator.check_token(obj, token):
            return invalid_url(self.request)

    def dispatch(self, request, *args, **kwargs):
        response = self.check_token()
        if response:
            return response
        return super(SignupLogicMixin, self).dispatch(request, *args, **kwargs)

    def login_user(self, email, password):
        user = auth.authenticate(
            username=email,
            password=password)
        auth.login(self.request, user)

    def get_success_url(self):
        return reverse('dashboard')


class SignupWizardView(SignupLogicMixin, NamedUrlSessionWizardView):
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'signup'))

    template_names = {
        'local-mind': 'registration/signup_step_local_mind.html',
        'profile': 'registration/signup_step_profile.html',
        'members': 'registration/signup_step_members.html',
        'partners': 'registration/signup_step_partners.html',
        'invites': 'registration/signup_step_invites.html',
    }

    def get_token_object(self, uid_int):
        try:
            reserved_email = ReservedEmail.objects.get(pk=uid_int)
        except ReservedEmail.DoesNotExist:
            reserved_email = None

        self.reserved_email = reserved_email
        return reserved_email

    def check_token(self):
        response = super(SignupWizardView, self).check_token()
        if response:
            return response

        if self.reserved_email:
            if self.reserved_email.local_mind.users.exists():
                return TemplateResponse(
                    self.request,
                    'registration/local_mind_already_signed_up.html',
                    context={
                        'email': self.reserved_email.email,
                        'reserved_email': self.reserved_email,
                        'local_mind': self.reserved_email.local_mind,
                    },
                    status=400)

    def get_template_names(self):
        return [self.template_names[self.steps.current]]

    def get_step_url(self, step):
        url_kwargs = self.kwargs.copy()
        url_kwargs['step'] = step
        return reverse(self.url_name, kwargs=url_kwargs)

    def get_form_initial(self, step):
        initial = super(SignupWizardView, self).get_form_initial(step)
        if step == 'local-mind':
            if self.reserved_email.local_mind:
                initial['name'] = self.reserved_email.local_mind.name
        return initial

    def get_context_data(self, **kwargs):
        kwargs['email'] = self.reserved_email.email
        return super(SignupWizardView, self).get_context_data(**kwargs)

    def done(self, form_list, **kwargs):
        local_mind_form, profile_form, members_form, partners_form, invites_form = form_list

        local_mind = local_mind_form.save(reserved_email=self.reserved_email)
        user = profile_form.save(
            email=self.reserved_email.email,
            local_mind=local_mind)

        members_form.save(local_mind=local_mind)
        partners_form.save(local_mind=local_mind, user=user)
        invites_form.save(local_mind=local_mind)

        self.login_user(
            user.email,
            profile_form.cleaned_data['password1'])

        return HttpResponseRedirect(self.get_success_url())


signup_forms = (
    ('local-mind', SignupLocalMindForm),
    ('profile', SignupProfileForm),
    ('members', SignupLocalMindMembersForm),
    ('partners', SignupPartnersForm),
    ('invites', SignupInviteForm),
)


signup_wizard = SignupWizardView.as_view(
    signup_forms,
    url_name='signup',
    done_step_name='complete')


class SignupUserProfileView(SignupLogicMixin, FormView):
    form_class = SignupUserProfileForm
    template_name = 'registration/signup_user_profile.html'

    def get_token_object(self, uid_int):
        try:
            obj = User.objects.get(pk=uid_int)
        except User.DoesNotExist:
            obj = None

        if obj and obj.date_joined is not None:
            obj = None

        self.user = obj
        return obj

    def get_context_data(self, **kwargs):
        kwargs['user'] = self.user
        return super(SignupUserProfileView, self).get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(SignupUserProfileView, self).get_form_kwargs()
        kwargs['instance'] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        self.login_user(
            user.email,
            form.cleaned_data['password1'])
        return HttpResponseRedirect(self.get_success_url())


signup_profile = SignupUserProfileView.as_view()


def invalid_url(request):
    return TemplateResponse(
        request,
        'registration/invalid_url.html',
        status=400)
