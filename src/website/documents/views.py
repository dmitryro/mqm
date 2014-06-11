# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from website.documents.models import Category, Document


class DocumentBase(object):
    categories = Category.public.all()
    paginate_by = 12

    def get_queryset(self, *args, **kwargs):
        queryset = super(DocumentBase, self).get_queryset(*args, **kwargs)
        if 'category_slug' in self.kwargs:
            category_slug = self.kwargs['category_slug']
            self.category = get_object_or_404(self.categories, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        else:
            self.category = None
        queryset = queryset.distinct()
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['category'] = self.category
        kwargs['categories'] = self.categories._clone()
        return super(DocumentBase, self).get_context_data(**kwargs)


class DocumentList(DocumentBase, ListView):
    queryset = Document.public.all()


document_list = DocumentList.as_view()


class DocumentDetail(DocumentBase, DetailView):
    queryset = Document.public.all()


document_detail = DocumentDetail.as_view()
