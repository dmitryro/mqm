from django import forms
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from website.views.generic import CommonViewMixin
from ..accounts.models import User, Skill


class SkillSearchForm(forms.Form):
    skill = forms.ModelChoiceField(
        label=_('Skill'),
        to_field_name='slug',
        queryset=Skill.objects.all(),
        empty_label='',
        widget=forms.Select(attrs={'class': 'form-control', 'data-placeholder': 'Search'}))

    def filter_queryset(self, queryset):
        if self.is_valid():
            queryset = queryset.filter(skills=self.cleaned_data['skill'])
        else:
            queryset = queryset.none()
        return queryset


class SkillSearchView(CommonViewMixin, TemplateView):
    queryset = User.objects.exclude(local_mind=None).exclude(date_joined=None).filter(is_active=True)
    form_class = SkillSearchForm
    template_name = 'search/skill_search.html'

    def get_context_data(self, **kwargs):
        if self.request.GET:
            form = self.form_class(self.request.GET)
        else:
            form = self.form_class()

        queryset = self.queryset._clone()
        queryset = form.filter_queryset(queryset)

        kwargs['form'] = form
        if form.is_valid():
            kwargs['skill'] = form.cleaned_data['skill']
        kwargs['members'] = queryset
        return super(SkillSearchView, self).get_context_data(**kwargs)


skill_search = SkillSearchView.as_view()
