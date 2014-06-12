from django.views.generic import TemplateView
from website.views.generic import CommonViewMixin


class DashboardView(CommonViewMixin, TemplateView):
    template_name = 'dashboard/my-dashboard.html'

    def get_context_data(self, **kwargs):
        return super(DashboardView, self).get_context_data(**kwargs)


dashboard = DashboardView.as_view()
