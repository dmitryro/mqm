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

    TRUSTEE = 'trustee'
    ADMIN = 'admin'
    SUPERUSER = 'superuser'
    PRIVILEGE_CHOICES = (
        (TRUSTEE, _('Trustee'),),
        (ADMIN, _('Admin'),),
        (SUPERUSER, _('Superuser'),),
    )

    slug = AutoSlugField(unique=True, populate_from=('first_name', 'last_name'))
    local_mind = models.ForeignKey('local_minds.LocalMind', null=True, blank=True, related_name='users')

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = EmailField(_('Email'), unique=True)
    job_title = models.CharField(_('Job Title'), max_length=50, blank=True)
    user_avatar = models.ImageField(_('Profile Image'), upload_to='users/avatars/', null=True, blank=True, help_text=_('Maximum size of 500kb. Only JPG, PNG accepted'))

    telephone = models.CharField(_('Contact Number'), max_length=50, blank=True)
    twitter = models.CharField(_('Twitter'), max_length=15, blank=True)

    biography = models.TextField(_('Biography'), max_length=350, blank=True, help_text=_('limited to 350 characters'))
    skills = models.TextField(_('Your Skills'), blank=True, help_text=_('comma seperated'))

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    privileges = models.CharField(_('Access level'), max_length=20, choices=PRIVILEGE_CHOICES)

    # If user does not have a date_joined yet, it is available for signup via
    # the invitation process still.
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now, null=True, blank=True)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return unicode(self.get_full_name())

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

    def get_token(self):
        return token_generator.make_token(self)

    def get_signup_url(self):
        return reverse('signup-profile', kwargs={
            'uidb36': int_to_base36(self.pk),
            'token': self.get_token()
        })

    def send_invitation(self):
        site = Site.objects.get_current()
        url = 'http://{site.domain}{path}'.format(
            site=site,
            path=self.get_signup_url())
        context = {
            'local_mind': self.local_mind,
            'user': self,
            'site': site,
            'signup_link': url,
        }
        email = TemplateEmail(
            to=[self.email],
            template='email/registration/invitation.html',
            context=context)
        email.send()


class Experience(models.Model):
    user = models.ForeignKey('User', related_name='experiences')
    experience = models.CharField(_('Experience'), max_length=250, help_text=_('Limited to 250 characters'))

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')

    def __unicode__(self):
        return self.experience


class Group(_Group):
    class Meta:
        proxy = True


class ReservedEmail(models.Model):
    '''
    Holds email addresses that are allowed to sign-up.
    '''

    email = EmailField(unique=True)
    local_mind = models.OneToOneField('local_minds.LocalMind')

    class Meta:
        verbose_name = _('Reserved Email')
        verbose_name_plural = _('Reserved Emails')

    def __unicode__(self):
        return self.email

    def get_token(self):
        return token_generator.make_token(self)

    def get_signup_url(self):
        return reverse('signup', kwargs={
            'uidb36': int_to_base36(self.pk),
            'token': self.get_token()
        })

    def send_signup_email(self):
        site = Site.objects.get_current()
        url = 'http://{site.domain}{path}'.format(
            site=site,
            path=self.get_signup_url())
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
