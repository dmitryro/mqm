# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.contrib.formtools.wizard.views import NamedUrlSessionWizardView
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import base36_to_int

from ..models import ReservedEmail
from .tokens import token_generator
from .forms import SignupLocalMindForm, SignupProfileForm, SignupStepThreeForm, SignupStepFourForm, SignupInviteForm


class SignupWizardView(NamedUrlSessionWizardView):
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'signup'))

    template_names = {
        'local-mind': 'registration/signup_step_local_mind.html',
        'profile': 'registration/signup_step_profile.html',
        'step3': 'registration/signup_step_step3.html',
        'step4': 'registration/signup_step_step4.html',
        'invites': 'registration/signup_step_invites.html',
    }

    def get_template_names(self):
        return [self.template_names[self.steps.current]]

    def get_step_url(self, step):
        url_kwargs = self.kwargs.copy()
        url_kwargs['step'] = step
        return reverse(self.url_name, kwargs=url_kwargs)

    def get_context_data(self, **kwargs):
        reserved_email = self.kwargs['reserved_email']
        kwargs['email'] = reserved_email.email
        return super(SignupWizardView, self).get_context_data(**kwargs)

    def done(self, form_list, **kwargs):
        return render_to_response('registration/signup_complete.html', {

        })


signup_forms = (
    ('local-mind', SignupLocalMindForm),
    ('profile', SignupProfileForm),
    ('step3', SignupStepThreeForm),
    ('step4', SignupStepFourForm),
    ('invites', SignupInviteForm),
)


wizard = SignupWizardView.as_view(
    signup_forms,
    url_name='signup',
    done_step_name='complete')


def signup_wizard(request, uidb36, token, step=None):
    try:
        uid_int = base36_to_int(uidb36)
        reserved_email = ReservedEmail.objects.get(pk=uid_int)
    except (ValueError, OverflowError, ReservedEmail.DoesNotExist):
        reserved_email = None

    if reserved_email is None or not token_generator.check_token(reserved_email, token):
        return invalid_url(request)

    return wizard(
        request,
        uidb36=uidb36,
        token=token,
        step=step,
        reserved_email=reserved_email)


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
