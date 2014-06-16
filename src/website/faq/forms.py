import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = (
            'question',
            'notifications',
            'privacy',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(QuestionForm, self).save(*args, **kwargs)
