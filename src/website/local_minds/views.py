# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from website.views.generic import CommonViewMixin
from ..accounts.models import User
from .models import LocalMind


class LocalMindDetailView(CommonViewMixin, DetailView):
    context_object_name = 'local_mind'
    queryset = LocalMind.objects.all()

    def get_object(self, queryset=None):
        if 'slug' not in self.kwargs:
            return self.request.user.local_mind
        return super(LocalMindDetailView, self).get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        kwargs['members'] = self.object.users.all()
        return super(LocalMindDetailView, self).get_context_data(**kwargs)


local_mind_detail = LocalMindDetailView.as_view()


class UserDetailView(CommonViewMixin, DetailView):
    template_name = 'local_minds/user_detail.html'
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = super(UserDetailView, self).get_queryset()
        queryset = queryset.filter(local_mind__slug=self.kwargs['local_mind_slug'])
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['local_mind'] = self.object.local_mind
        return super(UserDetailView, self).get_context_data(**kwargs)


user_detail = UserDetailView.as_view()
