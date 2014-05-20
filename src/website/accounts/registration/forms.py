from django.utils.translation import ugettext_lazy as _
import floppyforms as forms

from website.accounts.models import User
from website.local_minds.models import LocalMind


class SignupLocalMindForm(forms.ModelForm):
    accept_tos = forms.BooleanField(label=_('Terms'), required=True,
        help_text=_(
            'We (above LM) agree to all terms and conditions of the openhub '
            'site.'))

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
            'group_avatar',
        )


class SignupProfileForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Re-enter password'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'job_title',
            'skills',
            'image',
            'biography',
            'experience',
            'telephone',
            'mobile',
            'twitter',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(SignupProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SignupStepThreeForm(forms.Form):
    step3 = forms.CharField()


class SignupStepFourForm(forms.Form):
    step4 = forms.CharField()


class SignupInviteForm(forms.Form):
    invite = forms.CharField()
