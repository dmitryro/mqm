class PrivacyViewMixin(object):
    def get_queryset(self, *args, **kwargs):
        queryset = super(PrivacyViewMixin, self).get_queryset(*args, **kwargs)
        queryset = queryset.privacy(self.request.user)
        return queryset
