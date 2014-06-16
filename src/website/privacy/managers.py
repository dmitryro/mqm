from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet


class PrivacyFilter(object):
    def privacy(self, user):
        if not user.is_authenticated():
            return self.none()
        return self.filter(self._get_privacy_q(user))

    def _get_private_q(self, user):
        return Q(privacy='private', **{self.model.user_lookup: user})

    def _get_local_q(self, user):
        return Q(privacy='local', **{self.model.local_mind_lookup: user.local_mind})

    def _get_regional_q(self, user):
        if self.model.region_lookup:
            return Q(privacy='regional', **{self.model.region_lookup: user.local_mind.region})
        return Q()

    def _get_national_q(self, user):
        return Q(privacy='national')

    def _get_privacy_q(self, user):
        private = self._get_private_q(user)
        local = self._get_local_q(user)
        regional = self._get_regional_q(user)
        national = self._get_national_q(user)
        return private | local | regional | national


class PrivacyQuerySet(PrivacyFilter, QuerySet):
    pass


class PrivacyManager(PrivacyFilter, models.Manager):
    def get_query_set(self):
        return PrivacyQuerySet(self.model, using=self._db)
