# -*- coding: utf-8 -*-
import floppyforms.__future__ as forms
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from website.views.generic import CommonPrivacyViewMixin, ListCreateView
from ..local_minds.models import LocalMind
from .forms import QuestionForm
from .models import Question


class QuestionSearchForm(forms.Form):
    REGION_CHOICES = (
        ('', '---------',),
    ) + LocalMind.REGION_CHOICES
    region = forms.ChoiceField(choices=REGION_CHOICES, required=False)

    def get_queryset(self, queryset):
        region = self.cleaned_data.get('region')
        if region:
            queryset = queryset.filter(local_mind__region=region)
        return queryset


class QuestionListView(CommonPrivacyViewMixin, ListCreateView):
    form_class = QuestionForm
    queryset = Question.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = super(QuestionListView, self).get_queryset()
        region = self.request.GET.get('region')
        if region:
            queryset = queryset.filter(local_mind__region=region)
        return queryset

    def get_form_kwargs(self):
        kwargs = super(QuestionListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['my_questions'] = self.object_list.filter(user=self.request.user)
        context = super(QuestionListView, self).get_context_data(**kwargs)
        search_form = QuestionSearchForm(self.request.GET)
        if search_form.is_valid():
            context['object_list'] = search_form.get_queryset(context.pop('object_list'))
        context['search_form'] = search_form
        return context


question_list = QuestionListView.as_view()


class QuestionDetailView(CommonPrivacyViewMixin, DetailView):
    queryset = Question.objects.all()


question_detail = QuestionDetailView.as_view()
