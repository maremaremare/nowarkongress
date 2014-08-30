# -*- coding: utf-8 -*-
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import *
# Register your models here.


class MenuAdmin(MPTTModelAdmin):
    related_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }
    fieldsets = (
        ('', {
            'fields': ('title','parent',),
        }),
        ('Если это отдельная ссылка', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('path',),
        }),
        ('Если c пунктом меню связана категория или тема', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('content_type','object_id',),
        }),
        ('Если это главный пункт, а не подпункт', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('subtitle','order',),
        }),

    )

admin.site.register(MenuItem, MenuAdmin)