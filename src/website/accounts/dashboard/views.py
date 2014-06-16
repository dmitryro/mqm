from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, UpdateView
from website.views.generic import CommonViewMixin
from .forms import ProfileForm


class DashboardView(CommonViewMixin, TemplateView):
    template_name = 'dashboard/my-dashboard.html'

    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(**kwargs)


dashboard = DashboardView.as_view()


class ProfileFormView(CommonViewMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'dashboard/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('dashboard')


profile_form = ProfileFormView.as_view()
