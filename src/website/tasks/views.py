# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from website.views.generic import CommonViewMixin, ListCreateView
from .forms import TaskForm
from .models import Task


class TaskListView(CommonViewMixin, ListCreateView):
    form_class = TaskForm
    queryset = Task.objects.order_by('sort_value')

    def get_form_kwargs(self):
        kwargs = super(TaskListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['active_tasks'] = self.object_list.filter(done=False)
        kwargs['completed_tasks'] = self.object_list.filter(done=True)
        return super(TaskListView, self).get_context_data(**kwargs)


task_list = TaskListView.as_view()
