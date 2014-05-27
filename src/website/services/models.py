from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import (AutoSlugField, CreationDateTimeField,
    ModificationDateTimeField)
from ..privacy import PrivacyField


class Service(models.Model):
    TYPE_CHOICES = (
        ('type', _('Type (TODO: add more)'),),
    )

    local_mind = models.ForeignKey('local_minds.LocalMind', related_name='services')

    slug = AutoSlugField(unique=True, populate_from=('name',))
    name = models.CharField(_('Name'), max_length=50)
    type = models.CharField(_('Type'), max_length=20, choices=TYPE_CHOICES)

    users_count = models.PositiveIntegerField(_('Active Users'))

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __unicode__(self):
        return self.name
