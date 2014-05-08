import floppyforms as forms


class SignupLocalMindForm(forms.Form):
    local_mind = forms.CharField()


class SignupProfileForm(forms.ModelForm):
    profile = forms.CharField()


class SignupStepThreeForm(forms.Form):
    step3 = forms.CharField()


class SignupStepFourForm(forms.Form):
    step4 = forms.CharField()


class SignupInviteForm(forms.Form):
    invite = forms.CharField()
