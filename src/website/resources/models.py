from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from ..privacy import PrivacyMixin


class Resource(PrivacyMixin, models.Model):
    user = models.ForeignKey('accounts.User', verbose_name=_('Creator'))
    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='resources')

    slug = AutoSlugField(unique=True, populate_from=('name',))
    name = models.CharField(_('Resource'), max_length=50)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')

    def __unicode__(self):
        return self.name
