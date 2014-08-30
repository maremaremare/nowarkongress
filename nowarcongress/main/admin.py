# -*- coding: utf-8 -*-
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import *
from django.contrib.sites.models import Site


class SectionAdmin(OrderedModelAdmin):
    related_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }
    list_display = ('__unicode__', 'move_up_down_links',)

class PartnerAdmin(OrderedModelAdmin):
    list_display = ('__unicode__', 'move_up_down_links',)
  
admin.site.unregister(Site)

admin.site.register(SliderItem)
admin.site.register(HomePageSection, SectionAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Quote)
