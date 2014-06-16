import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'text',
            'due_date',
            'assigned_to',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = self.user.local_mind.users.all()

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(TaskForm, self).save(*args, **kwargs)
