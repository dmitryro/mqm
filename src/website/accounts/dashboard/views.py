from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, UpdateView
from website.views.generic import CommonViewMixin
from .forms import ProfileForm


class DashboardView(CommonViewMixin, TemplateView):
    template_name = 'dashboard/my-dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        questions = user.local_mind.questions.privacy(user)
        kwargs['questions'] = questions
        kwargs['my_questions'] = questions.filter(user=user)
        kwargs['my_tasks'] = user.tasks.order_by('-is_priority')
        partners = user.local_mind.partners.all()
        partners = partners.exclude(_latitude_postcode=None, _longitude_postcode=None)
        partners = partners.privacy(user)
        kwargs['map_list'] = partners
        kwargs['local_mind_users'] = user.local_mind.users.all()
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
