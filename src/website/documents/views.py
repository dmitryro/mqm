# -*- coding: utf-8 -*-
import floppyforms.__future__ as forms
from django.core.urlresolvers import reverse
from django.db.models import Count, Max, F
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from website.views.generic import CommonViewMixin, CommonPrivacyViewMixin, ListCreateView
from ..local_minds.models import LocalMind
from .forms import DocumentForm
from .models import Document, Category


class DocumentSearchForm(forms.Form):
    REGION_CHOICES = (
        ('', 'National',),
    ) + LocalMind.REGION_CHOICES
    region = forms.ChoiceField(choices=REGION_CHOICES, required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.order_by('name'),
        to_field_name='slug',
        empty_label=None,
        required=True)

    def filter_queryset(self, queryset):
        if self.is_valid():
            region = self.cleaned_data.get('region')
            if region:
                queryset = queryset.filter(local_mind__region=region)
            category = self.cleaned_data.get('category')
            if category:
                queryset = queryset.filter(categories=category)
        return queryset


category_queryset = Category.objects.order_by('name')
category_queryset = category_queryset.annotate(document_count=Count('documents'))
category_queryset = category_queryset.annotate(download_count=Count('documents__download_count'))
category_queryset = category_queryset.annotate(latest_upload_date=Max('documents__created'))


class CategoryListView(CommonViewMixin, ListCreateView):
    form_class = DocumentForm
    queryset = category_queryset

    def get_success_url(self):
        return self.request.path


category_list = CategoryListView.as_view()


class DocumentListView(CommonPrivacyViewMixin, ListCreateView):
    form_class = DocumentForm
    category_queryset = category_queryset
    queryset = Document.objects.order_by('-created')

    def dispatch(self, request, *args, **kwargs):
        self.search_form = DocumentSearchForm(request.GET)
        if not self.search_form.is_valid():
            return HttpResponseRedirect(reverse('documents-categories'))
        self.category = self.search_form.cleaned_data['category']
        return super(DocumentListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(DocumentListView, self).get_queryset()
        queryset = self.search_form.filter_queryset(queryset)
        return queryset

    def get_form_kwargs(self):
        kwargs = super(DocumentListView, self).get_form_kwargs()
        if self.category:
            kwargs.setdefault('initial', {}).update({'categories': [self.category.pk]})
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['regions'] = LocalMind.REGION_CHOICES
        kwargs['category_list'] = self.category_queryset
        kwargs['search_form'] = self.search_form
        return super(DocumentListView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return self.request.path


document_list = DocumentListView.as_view()


class DocumentDetailView(CommonPrivacyViewMixin, DetailView):
    category_queryset = category_queryset
    queryset = Document.objects.order_by('-created')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        document = Document.objects.filter(pk=self.object.pk)
        document.update(download_count=F('download_count') + 1)
        return HttpResponseRedirect(self.object.get_download_url())


document_detail = DocumentDetailView.as_view()
