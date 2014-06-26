import re
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


YOUTUBE_MATCH = re.compile(r'https?://(?:www\.)youtube\.com/watch.*v=.*$')
YOUTUBE_TOKENIZER = re.compile(r'(?P<domain>https?://(?:www\.)youtube\.com)/watch.*?[&?]v=(?P<video_id>[^&]*).*$')

VIMEO_MATCH = re.compile(r'https?://(?:www\.)vimeo\.com/(?:.+/)\d+$')
VIMEO_TOKENIZER = re.compile(r'https?://(?:www\.)vimeo\.com/(?:.+/)?(?P<video_id>d+)$')

VIMEO_IFRAME_URL = '//player.vimeo.com/video/{video_id}?title=0&amp;byline=0&amp;portrait=0'


@register.filter
def is_youtube_link(content):
    return bool(YOUTUBE_MATCH.match(content))


@register.filter
def is_vimeo_link(content):
    return bool(VIMEO_MATCH.match(content))


@register.filter
def youtube_iframe_url(content):
    match = YOUTUBE_TOKENIZER.match(content)
    groups = match.groupdict()
    content = '{domain}/embed/{video_id}?wmode=transparent'.format(**groups)
    return mark_safe(content.strip())


@register.filter
def vimeo_iframe_url(content):
    match = VIMEO_TOKENIZER.match(content)
    groups = match.groupdict()
    content = VIMEO_IFRAME_URL.format(**groups)
    return mark_safe(content.strip())


@register.filter
def render_youtube(content):
    content = '''
    <iframe width="560" height="315" src="{url}" frameborder="0" allowfullscreen></iframe>
    '''.format(url=youtube_iframe_url(content))
    return mark_safe(content.strip())


@register.filter
def render_vimeo(content):
    content = '''
    <iframe width="560" height="315" src="{url}" frameborder="0" allowfullscreen></iframe>
    '''.format(url=vimeo_iframe_url(content))
    return mark_safe(content.strip())


MEDIA_RENDERERS = (
    (YOUTUBE_MATCH, render_youtube),
    (VIMEO_MATCH, render_vimeo),
)



@register.filter
def render_embeded(content):
    content = content.strip()
    for regex, renderer in MEDIA_RENDERERS:
        if regex.match(content):
            return renderer(content)
    return mark_safe(content)
