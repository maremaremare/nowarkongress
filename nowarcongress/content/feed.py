# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import ContentItem

class LatestEntriesFeed(Feed):
    title = "Конгресс интеллигенции против войны"
    link = "/feed/"
    description = "Новости конгресса интеллигенции против войны"

    def items(self):
        return ContentItem.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    def item_categories(self, item):
        return (item.category.title,)

    def item_author_name(self, item):
        if item.author:
            return item.author.name
        else:
            return None

    def item_description(self, item):
            return '<h1>'+item.title+'</h1><p>'+item.text[:250]+'</p>'

    def item_author_link(self, item):
        if item.author:
            return item.author.get_absolute_url()
        else:
            return None
