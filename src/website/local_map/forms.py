import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Map


class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = (
            'name',
            'email',
            'website',
            'address',
            'postcode',
            'telephone',
            'category',
            'privacy',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MapForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(MapForm, self).save(*args, **kwargs)
