# Create your views here.

"""
Created on Jul 15, 2014
@author: 
"""

from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.context import RequestContext
from mqm.models import Question
# Create your views here.

class QuestionViewMixin(object):
    def get_context_data(self,**kwargs):
        questions = Question.objects.all()
        context = super(QuestionViewMixin,
                  self).get_context_data(**kwargs)
        quetion_media = []

        context['questions'] = questions
        context['is_paginated'] = True
        return context

class QuestionView(QuestionViewMixin, TemplateView):
        template_name = "question.html"


class QuestionDetailViewMixin(object):
    def get_context_data(self,**kwargs):
        context = super(QuestionDetailViewMixin,
                  self).get_context_data(**kwargs)
        return context


class QuestionDetailView(QuestionDetailViewMixin, TemplateView):
        template_name = "question_detail.html"

