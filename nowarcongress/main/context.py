# -*- coding: utf-8 -*-
from menu.models import MenuItem
from content.models import ContentCategory, ContentItem
from main.models import Partner
from person.models import Person
from haystack.forms import SearchForm


# def write_context(request):
#     return {'search':SearchForm, 'cal': QuerysetCalendar(ContentItem.objects.all(), 'date').formatmonth(now.year, now.month),  'comments': ThreadedComment.objects.order_by('-submit_date')[:3],  'partners': Partner.objects.all(), 'nodes': MenuItem.objects.all(), }

persons = Person.objects.filter(items__isnull=False).exclude(id=7).order_by("-items__date").distinct()

p = []

for x in persons:
    if x not in p:
        p.append(x)

def write_context(request):
    return {'blogs':p[:4],'news':ContentItem.objects.filter(category__slug='news')[:20], 'content_categories':ContentCategory.objects.all(), 'search':SearchForm,'partners': Partner.objects.all(), 'nodes': MenuItem.objects.all(), }
