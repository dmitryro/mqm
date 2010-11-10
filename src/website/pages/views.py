# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from website.pages import get_model

DEFAULT_TEMPLATE = 'pages/default.html'


def page(request, url):
    '''
    Page view.
    If the requested page does not exists it tries to append a slash or try to
    delete an existing slash and redirects to the new url.

    Models: `page.page`
    Templates: Uses the template defined by the ``template_name`` field,
    or `pages/default.html` if template_name is not defined.
    Context:
    page
        `page.page` object
    '''
    Page = get_model()
    if not url.startswith('/'):
        url = "/" + url
    try:
        p = Page.public.get(url=url)
    except ObjectDoesNotExist:
        if not url.endswith('/'):
            try:
                Page.public.get(url=url + '/')
                return HttpResponseRedirect(url + '/')
            except ObjectDoesNotExist:
                pass
        else:
            try:
                Page.public.get(url=url[:-1])
                return HttpResponseRedirect(url[:-1])
            except ObjectDoesNotExist:
                pass
        raise Http404
    if p.template_name:
        t = loader.select_template((p.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    c = RequestContext(request, {
        'page': p,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, Page, p.id)
    return response
