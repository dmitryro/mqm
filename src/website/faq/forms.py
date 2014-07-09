import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Answer, Question


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = (
            'answer',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.question = kwargs.pop('question', None)
        super(AnswerForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.question = self.question
        return super(AnswerForm, self).save(*args, **kwargs)


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = (
            'question',
            'notifications',
            'categories',
            'privacy',
        )
        widget = {
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'data-placeholder': 'Enter categories',
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(QuestionForm, self).save(*args, **kwargs)
