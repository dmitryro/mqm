# -*- coding: utf-8 -*-
import floppyforms.__future__ as forms
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from website.views.generic import CommonPrivacyViewMixin, ListCreateView, DetailCreateView
from ..local_minds.models import LocalMind
from .forms import AnswerForm, QuestionForm
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

    def get_context_data(self, **kwargs):
        kwargs['my_questions'] = self.get_queryset().filter(user=self.request.user)
        context = super(QuestionListView, self).get_context_data(**kwargs)
        search_form = QuestionSearchForm(self.request.GET)
        if search_form.is_valid():
            context['question_list'] = search_form.get_queryset(context.pop('question_list'))
            context['object_list'] = context['question_list']
        context['search_form'] = search_form

        context['answer_form'] = AnswerForm(user=self.request.user)
        return context


question_list = QuestionListView.as_view()


class QuestionDetailView(CommonPrivacyViewMixin, DetailCreateView):
    form_class = AnswerForm
    queryset = Question.objects.all()

    def get_form_kwargs(self):
        kwargs = super(QuestionDetailView, self).get_form_kwargs()
        kwargs['question'] = self.object
        del kwargs['instance']
        return kwargs


question_detail = QuestionDetailView.as_view()
