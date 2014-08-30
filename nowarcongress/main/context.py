# -*- coding: utf-8 -*-
from menu.models import MenuItem
from content.models import Topic, ContentItem
from main.models import Partner
from threadedcomments import ThreadedComment



# from calendar import HTMLCalendar
# from datetime import date
# from itertools import groupby


# from django.utils.html import conditional_escape as esc
# from django.template import defaultfilters

# #formatted_date = defaultfilters.date(usr.date_joined, "SHORT_DATETIME_FORMAT")

# class QuerysetCalendar(HTMLCalendar):


#     def __init__(self, queryset, field):

#         self.field = field
#         super(QuerysetCalendar, self).__init__()
#         self.queryset_by_date = self.group_by_day(queryset)

#     def formatday(self, day, weekday):
#         if day != 0:
#             cssclass = self.cssclasses[weekday]

#             if day in self.queryset_by_date:
#                 cssclass += ' filled'

#                 return self.day_cell(cssclass, '%s' % ('<a href="/archive/'+str(now.year)+'/'+str(now.month)+'/'+str(day)+'">'+str(day)+'</a>'))
#             return self.day_cell(cssclass, day)
#         return self.day_cell('noday', ' ')


#     def formatweekday(self, day):
#     	return u'<th scope="col">'+day+u'</th>'

#     def formatweekheader(self):
#         """
#         Return a header for a week as a table row.
#         """
#         s = ''.join(self.formatweekday(i) for i in [u'Пон', u'Вт', u'Ср', u'Чт', u'Пт', u'Сб', u'Вс'])
#         return u'<thead><tr>{0}</tr></thead>'.format(s)

#     def formatmonth(self, theyear, themonth, withyear=True):
#         """
#         Return a formatted month as a table.
#         """
#         v = []
#         a = v.append
#         a('<table border="0" cellpadding="0" cellspacing="0" class="month" id="wp-calendar">')
#         a('\n')
#         a(u'<caption>'+defaultfilters.date(now, "F Y")+u'</caption>')
#         a('\n')
#         a(self.formatweekheader())
#         a('\n')
#         for week in self.monthdays2calendar(theyear, themonth):
#             a(self.formatweek(week))
#             a('\n')
#         a('</table>')
#         a('\n')
#         return ''.join(v)

#     def group_by_day(self, queryset):
#         field = lambda item: getattr(item, self.field).day
#         return dict(
#             [(day, list(items)) for day, items in groupby(queryset, field)]
#         )

#     def day_cell(self, cssclass, body):
#         return '<td class="%s">%s</td>' % (cssclass, body)


# import datetime

# now = datetime.datetime.now()

# from datetime import datetime
# date_joined = datetime.now()
# from django.utils import formats
# formatted_datetime = formats.date_format(date_joined, "SHORT_DATETIME_FORMAT")




# LANGUAGE_CODE           = 'ru-Rus'
# FIRST_DAY_OF_WEEK       = 0     # 0 is Sunday
# # Convert to calendar module, where 0 is Monday :/
# FIRST_DAY_OF_WEEK_CAL   = (FIRST_DAY_OF_WEEK - 1) % 7

# # figure locale name
# LOCAL_LANG              = LANGUAGE_CODE.split('-')[0]
# LOCAL_COUNTRY           = LANGUAGE_CODE.split('-')[1].upper()
# LOCALE_NAME             = LOCAL_LANG + '_' + LOCAL_COUNTRY + '.UTF8'

from haystack.forms import SearchForm


# def write_context(request):
#     return {'search':SearchForm, 'cal': QuerysetCalendar(ContentItem.objects.all(), 'date').formatmonth(now.year, now.month),  'comments': ThreadedComment.objects.order_by('-submit_date')[:3],  'partners': Partner.objects.all(), 'nodes': MenuItem.objects.all(), }

def write_context(request):
    return {'search':SearchForm,'partners': Partner.objects.all(), 'nodes': MenuItem.objects.all(), }
