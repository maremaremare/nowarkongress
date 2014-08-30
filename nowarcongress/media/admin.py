from django.contrib import admin
from .models import *


from filebrowser.widgets import FileInput

class PhotoOptions(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')
    formfield_overrides = {
        models.ImageField: {'widget': FileInput},
    }

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class VideoInline(admin.TabularInline):
    model = Video
    extra = 0

class RelatedMediaAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline, ]

admin.site.register(Photo, PhotoOptions)
admin.site.register(Video)
