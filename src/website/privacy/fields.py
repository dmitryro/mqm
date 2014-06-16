from django.db import models
from django.utils.translation import ugettext_lazy as _


PRIVACY_CHOICES = (
    ('national', _('National')),
    ('private', _('Private')),
    ('local', _('Local')),
    ('regional', _('Regional')),
)


class PrivacyField(models.CharField):
    def __init__(self, verbose_name=_('Privacy'), *args, **kwargs):
        kwargs.setdefault('choices', PRIVACY_CHOICES)
        kwargs.setdefault('default', 'national')
        kwargs.setdefault('max_length', 12)
        super(PrivacyField, self).__init__(verbose_name, *args, **kwargs)


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^website\.privacy\.fields\.PrivacyField"])
