from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django_compositeform import CompositeModelForm, ForeignKeyFormField
import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm, formfield_callback

from website.accounts.models import User
from website.local_minds.forms import PersonForm
from website.local_minds.models import LocalMind


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'job_title',
            'skills',
            'user_avatar',
            'biography',
            'telephone',
            'twitter',
        )

    def clean_twitter(self):
        value = self.cleaned_data['twitter']
        if value:
            value = value.lstrip('@')
        return value


class LocalMindForm(CompositeModelForm):
    formfield_callback = formfield_callback

    ceo_one = ForeignKeyFormField(PersonForm)
    ceo_two = ForeignKeyFormField(PersonForm)
    chair = ForeignKeyFormField(PersonForm)

    class Meta:
        model = LocalMind
        fields = (
            'name',
            'region',
            'address',
            'postcode',
            'income_restricted',
            'charity_no',
            'charity_type',
            'email',
            'telephone',
            'website',
            'income_unrestricted',
            'reserves',
            'deficit',
            'statement',
            'hours',
            'group_avatar',
            'staff_count',
            'trustees_count',
            'volunteers_count',
            'trustees_active',
            'area_of_benefit',
            'average_volunteer_hours',
        )


class PasswordChangeForm(_PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget = forms.PasswordInput()
