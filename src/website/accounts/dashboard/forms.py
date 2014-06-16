import floppyforms as forms
from floppyforms.__future__.models import ModelForm

from website.accounts.models import User


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
