from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView, UpdateView
from website.views.generic import CommonViewMixin
from website.news.models import PositiveNews
from website.local_minds.models import LocalMind
from ..forms import InvitationForm
from .forms import LocalMindForm, ProfileForm


class DashboardView(CommonViewMixin, TemplateView):
    template_name = 'dashboard/my-dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        questions = user.local_mind.questions.privacy(user)
        kwargs['questions'] = questions
        kwargs['my_questions'] = questions.filter(user=user)
        kwargs['my_tasks'] = user.tasks.order_by('-is_priority')
        kwargs['positivenews_list'] = PositiveNews.objects.privacy(user)
        partners = user.local_mind.partners.all()
        partners = partners.exclude(_latitude_postcode=None, _longitude_postcode=None)
        partners = partners.privacy(user)
        kwargs['map_list'] = partners

        net_works = LocalMind.objects.all()
        net_works = net_works.exclude(_latitude_postcode=None, _longitude_postcode=None)
        kwargs['net_works'] = net_works

        kwargs['local_mind_users'] = user.local_mind.users.all()
        return super(DashboardView, self).get_context_data(**kwargs)


dashboard = DashboardView.as_view()


class LocalMindUpdateView(CommonViewMixin, UpdateView):
    form_class = LocalMindForm
    template_name = 'dashboard/local_mind_form.html'
    context_object_name = 'local_mind'

    def get_object(self, queryset=None):
        return self.request.user.local_mind

    def get_success_url(self):
        return reverse('dashboard')


local_mind_form = LocalMindUpdateView.as_view()


class ProfileUpdateView(CommonViewMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'dashboard/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('dashboard')


profile_form = ProfileUpdateView.as_view()


class InviteFormView(CommonViewMixin, FormView):
    form_class = InvitationForm
    template_name = 'dashboard/invitation_form.html'

    def form_valid(self, form):
        form.save(local_mind=self.request.user.local_mind)
        return super(FormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


invite_form = InviteFormView.as_view()
