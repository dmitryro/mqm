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
        if self.user.privileges == self.user.SUPERUSER:
            self.fields['assigned_to'].queryset = self.user.local_mind.users.all()
            self.initial.setdefault('assigned_to', self.user)
        else:
            del self.fields['assigned_to']

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        if self.user.privileges != self.user.SUPERUSER:
            self.instance.assigned_to = self.user
        return super(TaskForm, self).save(*args, **kwargs)
