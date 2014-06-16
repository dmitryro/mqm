# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter
def concat(value, arg):
    value = unicode(value)
    arg = unicode(arg)
    return value + arg
