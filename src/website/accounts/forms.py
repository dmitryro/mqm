# -*- coding: utf-8 -*-

import floppyforms as forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=_("Email"), max_length=75)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)


class SignupForm(forms.Form):
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']
        raise forms.ValidationError(_("""
            Sorry, but we don't recognize this email address. We need to have
            your email in our database in order to allow signup. Please make
            sure that you used the same email address here as you use for
            communications with minds.
            """))
        return email
