from django.conf import settings
from django.db import models
import geocoder


class PostcodeLocationMixin(models.Model):
    _latitude_postcode = models.CharField(max_length=32, null=True, blank=True)
    _longitude_postcode = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def latitude(self):
        return self._latitude_postcode

    @property
    def longitude(self):
        return self._longitude_postcode

    def calculate_position(self, commit=False):
        if self.postcode:
            response = geocoder.google(
                '{}, United Kingdom'.format(self.postcode),
                api_key=settings.GOOGLE_MAPS_API_KEY)
            assert response.ok, response.status
            self._latitude_postcode = response.latitude
            self._longitude_postcode = response.longitude
        else:
            self._latitude_postcode = None
            self._longitude_postcode = None

    def save(self, *args, **kwargs):
        self.calculate_position()
        return super(PostcodeLocationMixin, self).save(*args, **kwargs)

