# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.models import Group as _Group
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from template_email import TemplateEmail

from website.utils.fields import EmailField
from .registration.tokens import token_generator


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    slug = AutoSlugField(unique=True, populate_from=('first_name', 'last_name'))

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = EmailField(_('email address'), unique=True)
    job_title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='users/avatars/', null=True, blank=True)
    telephone = models.CharField(max_length=50, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class Group(_Group):
    class Meta:
        proxy = True


class ReservedEmail(models.Model):
    '''
    Holds email addresses that are allowed to sign-up.
    '''

    email = EmailField(unique=True)

    class Meta:
        verbose_name = _('Reserved Email')
        verbose_name_plural = _('Reserved Emails')

    def __unicode__(self):
        return self.email

    def send_signup_email(self):
        site = Site.objects.get_current()
        token = token_generator.make_token(self)
        path = reverse('signup', kwargs={
            'uidb36': int_to_base36(self.pk),
            'token': token
        })
        url = 'http://{site.domain}{path}'.format(
            site=site,
            path=path)
        context = {
            'email': self.email,
            'site': site,
            'signup_link': url,
        }
        email = TemplateEmail(
            to=[self.email],
            template='email/registration/signup.html',
            context=context)
        email.send()
