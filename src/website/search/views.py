from django.views.generic import TemplateView

from website.views.generic import CommonViewMixin
from ..accounts.models import User
from .forms import SkillSearchForm


class SkillSearchView(CommonViewMixin, TemplateView):
    queryset = User.active.all()
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
