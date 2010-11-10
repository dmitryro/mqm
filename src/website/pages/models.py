# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django_publicmanager.managers import GenericPublicManager, PublicOnlyManager
from mediastore.fields import MultipleMediaField


class Page(models.Model):
    url = models.CharField(_('URL'), max_length=150, db_index=True)
    title = models.CharField(_('title'), max_length=255)
    content = models.TextField(_(u'content'))
    media = MultipleMediaField(sorted=True,
        related_name='page_media',
        null=True, blank=True)

    template_name = models.CharField(_('template name'),
        choices=(
            ('pages/simple_text.html', _('simple text')),
            ('pages/simple_media.html', _('simple media')),
            ('pages/combined.html', _('combination')),
        ),
        max_length=120, blank=True, help_text=_(
            u'You can use a different template than the default '
            u'one to render this page. Leave blank to fall back '
            u'to the default template.'
    ))
    is_public = models.BooleanField(_(u'is public?'), default=True, help_text=_(
        u'The page is only viewable if this checkbox is set.'
    ))
    pub_date = models.DateTimeField(_(u'Publication date'),
        default=datetime.now, help_text=_(
            u'This page is only viewable if the publication date is in the '
            u'past.'
    ))

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    objects = GenericPublicManager()
    public = PublicOnlyManager()

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('url',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url
