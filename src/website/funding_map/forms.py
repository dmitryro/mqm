import floppyforms.__future__ as forms
from floppyforms.__future__.models import ModelForm

from .models import Funding


class FundingForm(ModelForm):
    class Meta:
        model = Funding
        fields = (
            'title',
            'start_date',
            'end_date',
            'description',
            'telephone',
            'email',
            'website',
            'postcode',
            'privacy',
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(FundingForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.user = self.user
        self.instance.local_mind = self.user.local_mind
        return super(FundingForm, self).save(*args, **kwargs)

