# -*- coding: utf-8 -*-

import floppyforms as forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
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
                    Sorry, but we don't recognize this email address. We need to have
                    your email in our database in order to allow signup. Please make
                    sure that you used the same email address here as you use for
                    communications with minds.
                    """))
            return reserved.get()
        return email

    def save(self):
        reserved = self.cleaned_data['email']
        reserved.send_signup_email()
