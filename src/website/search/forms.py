from django import forms
from django.utils.translation import ugettext_lazy as _

from ..accounts.models import Skill


class SkillSearchForm(forms.Form):
    skill = forms.ModelChoiceField(
        label=_('Skill'),
        to_field_name='slug',
        queryset=Skill.objects.all(),
        empty_label='',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'data-placeholder': 'Search'
        }))

    def filter_queryset(self, queryset):
        if self.is_valid():
            queryset = queryset.filter(skills=self.cleaned_data['skill'])
        else:
            queryset = queryset.none()
        return queryset
