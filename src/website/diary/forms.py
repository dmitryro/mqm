import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'title',
            'start',
            'end',
            'location',
            'postcode',
            'privacy',
        )
        widgets = {
            'start': forms.SplitDateTimeWidget,
            'end': forms.SplitDateTimeWidget,
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EventForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(EventForm, self).save(*args, **kwargs)
