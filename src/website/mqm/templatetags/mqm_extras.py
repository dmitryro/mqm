import logging
import re
import sys
from urlparse import urlparse
from django.template import Library, Node, NodeList, TemplateSyntaxError
from django.utils.encoding import smart_str
from property.models import Property
from tagging.models import Tag, TaggedItem
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

kw_pat = re.compile(r'^(?P<key>[\w]+)=(?P<value>.+)$')
logger = logging.getLogger('sorl.thumbnail')


@register.simple_tag
def mqm_meta(a, b, *args, **kwargs):
    pass


 
