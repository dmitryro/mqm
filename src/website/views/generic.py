from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import ModelFormMixin
from website.privacy import PrivacyViewMixin


class LoginRequiredMixin(object):
    login_required = True

    def access_denied(self, request):
        return HttpResponseRedirect(
            '{login}?next={next}'.format(
                login=reverse('login'),
                next=request.path))

    def dispatch(self, request, *args, **kwargs):
        if self.login_required:
            if not request.user.is_authenticated() or request.user.local_mind is None:
                return self.access_denied(request)
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class CommonViewMixin(LoginRequiredMixin):
    pass


class CommonPrivacyViewMixin(LoginRequiredMixin, PrivacyViewMixin):
    pass


class CreateMixin(ModelFormMixin):
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        if not hasattr(self, 'object'):
            self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        if not hasattr(self, 'object'):
            self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DetailCreateView(CreateMixin, DetailView):
    show_form = False

    def dispatch(self, request, *args, **kwargs):
        self.show_form = kwargs.pop('show_form', self.show_form)
        return super(DetailCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(DetailCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(DetailCreateView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(DetailCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_object_name(self, obj):
        return DetailView.get_context_object_name(self, obj)

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['show_form'] = self.show_form or context['form'].is_bound
        return context


class ListCreateView(CreateMixin, ListView):
    show_form = False

    def dispatch(self, request, *args, **kwargs):
        self.show_form = kwargs.pop('show_form', self.show_form)
        return super(ListCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super(ListCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super(ListCreateView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ListCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_object_name(self, object_list):
        return ListView.get_context_object_name(self, object_list)

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, object_list=self.object_list, **kwargs)
        context['show_form'] = self.show_form or context['form'].is_bound
        return context
