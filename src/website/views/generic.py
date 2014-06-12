from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


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
