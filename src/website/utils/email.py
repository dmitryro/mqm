# -*- coding: utf-8 -*-
import os
from django.core.mail import get_connection
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Context, RequestContext
from django.template.loader import get_template


def send_template_mail(template_name, to, from_email=None, extra_context=None,
    request=None, subject_template=None, html=False, **kwargs):
    default_context = {
        'site': Site.objects.get_current(),
    }
    if request:
        context = RequestContext(request, default_context)
    else:
        context = Context(default_context)
    if extra_context:
        context.update(extra_context)
    if not subject_template:
        subject_template = '%s_subject%s' % os.path.splitext(template_name)
    subject = get_template(subject_template)
    body = get_template(template_name)

    subject = (''.join(subject.render(context).splitlines())).strip()
    body = body.render(context)
    from_email = from_email or settings.DEFAULT_FROM_EMAIL

    connection = get_connection()

    message = EmailMessage(subject, body, from_email, to, connection=connection)
    if html:
        message.content_subtype = 'html'
    return message.send()
