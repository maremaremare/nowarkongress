# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import ContentAdminForm
import facebook

from django.forms import CheckboxSelectMultiple
from ordered_model.admin import OrderedModelAdmin
from media.admin import RelatedMediaAdmin
#from django_monitor.admin import MonitorAdmin
from moderation.admin import ModerationAdmin
from autocomplete_light.contrib.taggit_tagfield import TagField, TagWidget
import logging

from nowarcongress.settings.secrets import PAGE_ACCESS_TOKEN
from import_export.admin import ImportExportModelAdmin
# Get an instance of a logger
logger = logging.getLogger('my')

def post_to_facebook(self, request, queryset):
    user = request.user
    auth = user.social_auth.first()
    graph = facebook.GraphAPI(PAGE_ACCESS_TOKEN)
    for x in queryset:
        try:
            logger.info(x.get_absolute_url())
            graph.put_object('306238759557765', 'feed', link='http://nowarcongress.com'+x.get_absolute_url(), message=x.facebook_description)
        except:
            raise

    self.message_user(request, u"Перепост в фейсбук успешно выполнен")


    
post_to_facebook.short_description = u"Опубликовать в фейсбуке"

class ContentAdmin(RelatedMediaAdmin, ModerationAdmin):
    actions = [post_to_facebook]
    form = ContentAdminForm
    list_display = ('title', 'author', 'category', 'topic', 'get_moderation_text', 'date')
    list_filter = ('category', 'topic')
    fieldsets = (
        ('', {
            'fields': ('title','date', 'text','category','author','source','topic','tags','comments_enabled', 'facebook_description'),
        }),
        ('Если это заявление', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('petition',),
        }),
        ('Если это надо связать с сессией конгресса', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('event',),
        }),

    )


class CategoryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class SidebarAdmin(OrderedModelAdmin):
    related_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }
    list_display = ('title', 'move_up_down_links',)

class PetitionAdmin(ImportExportModelAdmin):
    raw_id_fields = ("outerparticipants",)
    resource_class = PetitionResource
    

class SignatureAdmin(ImportExportModelAdmin):
    search_fields = ['second_name', 'first_name']
    resource_class = SignatureResource
    list_display = ('is_shown', '__unicode__', 'first_name', 'second_name', 'occupation', 'email', 'city','order')
    list_editable = ('first_name','order', 'second_name','email','city','is_shown','occupation')
    list_display_links = ('__unicode__',)
    ordering = ['-added']

admin.site.register(ContentItem, ContentAdmin)
admin.site.register(ContentCategory, CategoryAdmin)
admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(Petition, PetitionAdmin)
admin.site.register(OuterParticipant, SignatureAdmin)
admin.site.register(SidebarItem, SidebarAdmin)