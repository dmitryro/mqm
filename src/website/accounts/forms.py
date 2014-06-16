# -*- coding: utf-8 -*-

import floppyforms as forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm as _PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _
from template_email import TemplateEmail
from .models import User, ReservedEmail


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email"), max_length=75)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)


class SignupForm(forms.Form):
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            email = email.lower()
            already_signedup = User.objects.filter(email=email).exists()
            if already_signedup:
                raise forms.ValidationError(_("""
                    Seems like you have already signed up with this email
                    address. You can continue by logging into your account.
                    """))
            reserved = ReservedEmail.objects.filter(email=email)
            if not reserved:
                raise forms.ValidationError(_("""
                    This email has not be recognised - please recheck your email address and enter again
                    """))
            return reserved.get()
        return email

    def save(self):
        reserved = self.cleaned_data['email']
        reserved.send_signup_email()


class PasswordResetForm(_PasswordResetForm):
    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        for user in self.users_cache:
            if not domain_override:
                site = get_current_site(request)
            context = {
                'email': user.email,
                'site': site,
                'uidb36': int_to_base36(user.pk),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }
            email = TemplateEmail(
                to=[user.email],
                template='email/registration/password_forgotten.html',
                context=context)
            email.send()
