from datetime import date
import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import PositiveNews


class PositiveNewsForm(ModelForm):
    class Meta:
        model = PositiveNews
        fields = (
            'title',
            'date',
            'description',
            'source',
            'privacy',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PositiveNewsForm, self).__init__(*args, **kwargs)
        self.initial.setdefault('date', date.today())

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(PositiveNewsForm, self).save(*args, **kwargs)
