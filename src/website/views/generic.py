class LoginRequiredMixin(object):
    login_required = True
    access_denied_template = '403.html'

    def access_denied(self, request):
        return self.response_class(
            request=self.request,
            template=self.access_denied_template,
            status=403)

    def dispatch(self, request, *args, **kwargs):
        if self.login_required and not request.user.is_authenticated():
            return self.access_denied(request)
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class CommonViewMixin(LoginRequiredMixin):
    pass
