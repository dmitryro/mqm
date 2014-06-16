from django.db import models
from .fields import PrivacyField
from .managers import PrivacyManager


class PrivacyMixin(models.Model):
    user_lookup = 'user'
    local_mind_lookup = 'local_mind'
    region_lookup = None

    privacy = PrivacyField()

    objects = PrivacyManager()

    class Meta:
        abstract = True
