# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View
from website.views.generic import CommonViewMixin, ListCreateView
from .forms import TaskForm
from .models import Task


class TaskListView(CommonViewMixin, ListCreateView):
    form_class = TaskForm
    queryset = Task.objects.order_by('sort_value')

    def get_queryset(self, *args, **kwargs):
        queryset = super(TaskListView, self).get_queryset()
        queryset = queryset.filter(assigned_to=self.request.user)
        return queryset

    def get_form_kwargs(self):
        kwargs = super(TaskListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['active_tasks'] = self.object_list.filter(done=False)
        kwargs['completed_tasks'] = self.object_list.filter(done=True)
        return super(TaskListView, self).get_context_data(**kwargs)


task_list = TaskListView.as_view()


class TaskDoneView(CommonViewMixin, View):
    def post(self, request, pk, done):
        tasks = Task.objects.filter(assigned_to=request.user)
        try:
            task = tasks.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
        task.mark_as_done(done=done)
        return HttpResponse()


task_done = TaskDoneView.as_view()
