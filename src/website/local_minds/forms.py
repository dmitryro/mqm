from floppyforms.__future__.models import ModelForm

from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = (
            'name',
            'ethnicity',
            'gender',
            'email',
            'telephone',
        )

