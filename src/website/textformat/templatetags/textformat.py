# -*- coding: utf-8 -*-
from django import template
from django.utils.encoding import force_unicode
from django.utils.html import escape, urlize
from django.utils.safestring import mark_safe
from postmarkup import render_bbcode


register = template.Library()


def render_markup(text):
    escaped_text = escape(text)
    formated_text = render_bbcode(escaped_text)
    formated_text = urlize(formated_text)
    return mark_safe(formated_text)


@register.filter
def textformat(value):
    if not value:
        return ''
    value = force_unicode(value)
    return render_markup(value)
