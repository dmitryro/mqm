from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
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
        if self.login_required and not request.user.is_authenticated():
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
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ListCreateView(CreateMixin, ListView):
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
        return ListView.get_context_data(self, object_list=self.object_list, **kwargs)
