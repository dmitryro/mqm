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
from .forms import SignupLocalMindForm, SignupProfileForm, SignupLocalMindMembersForm, SignupPartnersForm, SignupInviteForm


class SignupWizardView(NamedUrlSessionWizardView):
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'signup'))

    template_names = {
        'local-mind': 'registration/signup_step_local_mind.html',
        'profile': 'registration/signup_step_profile.html',
        'members': 'registration/signup_step_members.html',
        'partners': 'registration/signup_step_partners.html',
        'invites': 'registration/signup_step_invites.html',
    }

    def dispatch(self, request, *args, **kwargs):
        uidb36 = kwargs['uidb36']
        token = kwargs['token']

        try:
            uid_int = base36_to_int(uidb36)
            self.reserved_email = ReservedEmail.objects.get(pk=uid_int)
        except (ValueError, OverflowError, ReservedEmail.DoesNotExist):
            self.reserved_email = None

        if self.reserved_email is None or not token_generator.check_token(self.reserved_email, token):
            return invalid_url(request)

        return super(SignupWizardView, self).dispatch(request, *args, **kwargs)

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
            reserved_email=self.reserved_email,
            local_mind=local_mind)

        members_form.save(local_mind=local_mind)
        partners_form.save(local_mind=local_mind, user=user)
        invites_form.save(local_mind=local_mind)

        return render_to_response('registration/signup_complete.html', {

        })


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
