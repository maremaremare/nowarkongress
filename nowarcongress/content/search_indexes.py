# -*- coding: utf-8 -*-
import datetime
from haystack import indexes
from .models import ContentItem


class ContentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.DateTimeField(model_attr='date')

    def prepare_term(self, term):
        return term[:245]

    def get_model(self):
        return ContentItem

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date__lte=datetime.datetime.now())
