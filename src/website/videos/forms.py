import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Video


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = (
            'title',
            'date',
            'description',
            'url',
            'privacy',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(VideoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(VideoForm, self).save(*args, **kwargs)
