# -*- coding: utf-8 -*-
from django import forms
from content.models import ContentItem, ContentCategory
from media.models import Photo, Video
from person.models import Person
import autocomplete_light
from autocomplete_light.contrib import taggit_tagfield
from django.forms.models import inlineformset_factory

class ContentForm(forms.ModelForm):
    tags = taggit_tagfield.TagField(widget=taggit_tagfield.TagWidget('TagAutocomplete'), required = False, label=u'Метки')
    #tags.label = u'Метки'

    class Meta:
        fields = ('category', 'title', 'date', 'text', 'topic', 'tags', 'comments_enabled')
        model = ContentItem
        widgets = {
            'tags': autocomplete_light.TextWidget('TagAutocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['category'].queryset = ContentCategory.objects.filter(usergenerated=True)

PhotoFormSet = inlineformset_factory(ContentItem, Photo, extra=1, max_num=1)


class ContentAdminForm(forms.ModelForm):
    tags = taggit_tagfield.TagField(widget=taggit_tagfield.TagWidget('TagAutocomplete'), required = False, label=u'Метки')
    class Meta:
        model = ContentItem
        widgets = {
            'tags': autocomplete_light.TextWidget('TagAutocomplete'),
        }