# -*- coding: utf-8 -*-
import random
from django import template


register = template.Library()


@register.simple_tag
def obfuscate_email(email):
    code_list = []
    for c in email:
        d = ord(c)
        x = random.randint(0, d)
        code_list.append("%d+%d" % (x, d-x))
    return '<script type="text/javascript">document.write(String.fromCharCode(%s))</script>' % \
        ",".join(code_list)
