# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from content.models import ContentItem
from .models import *

from taggit.models import Tag, TaggedItem
# Create your views here.

import logging
from haystack.views import SearchView
# Get an instance of a logger
logger = logging.getLogger('my')


class HomePageView(SearchView, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['slider_items'] = SliderItem.objects.all()
       
        context['section_list'] = HomePageSection.objects.all()
        context['quote'] = Quote.objects.all()
        return context


class TagListView(TemplateView):
    template_name = 'list_tags.html'

    def get_context_data(self, **kwargs):
        tag = self.kwargs['tag']
        tagname = Tag.objects.get(slug=tag).name

        context = super(TagListView, self).get_context_data(**kwargs)
        context['listtitle'] = u'Все материалы с меткой «' + tagname + u'»'
        context['object_list'] = TaggedItem.objects.filter(
            tag__slug=self.kwargs['tag'])
        context['actualsidebar'] = ActualSlider.objects.latest('date')
        return context

from django.views.generic.dates import DayArchiveView
from datetime import datetime
from django.template import defaultfilters


class ItemDayArchiveView(DayArchiveView):
    queryset = ContentItem.objects.all()
    date_field = "date"
    make_object_list = True
    allow_future = True
    template_name = 'list_archive.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDayArchiveView, self).get_context_data(**kwargs)
        if len(self.object_list) > 3:
            context['actualsidebar'] = ActualSlider.objects.latest('date')
        context['advs'] = ContentItem.objects.filter(
            category__slug='recommendations')[:1]
        cr_date = datetime(
            int(self.get_year()), int(self.get_month()), int(self.get_day()))
        context['listtitle'] = defaultfilters.date(cr_date, "d E Y")
        return context


class MainAboutView(TemplateView):
    template_name = 'main_about.html'

    def get_context_data(self, **kwargs):
        context = super(MainAboutView, self).get_context_data(**kwargs)

        context['petitions'] = ContentItem.objects.filter(topic__id=3)
        context['members_about'] = ContentItem.objects.filter(topic__id=9)

        return context