# -*- coding: utf-8 -*-
from django import forms
from content.models import ContentItem, ContentCategory
from media.models import Photo, Video
from .models import Person
import autocomplete_light
from autocomplete_light.contrib import taggit_tagfield
from django.forms.models import inlineformset_factory
import datetime

class ContentForm(forms.ModelForm):
    #date = forms.DateTimeField(initial = datetime.datetime.now) 
    tags = taggit_tagfield.TagField(widget=taggit_tagfield.TagWidget('TagAutocomplete'), required=False, label=u'Метки')

    class Meta:
        fields = ('category', 'date', 'title', 'text', 'topic', 'tags', 'comments_enabled')
        model = ContentItem
        widgets = {
            'tags': autocomplete_light.TextWidget('TagAutocomplete'),
        }
        #initial = {'date': datetime.datetime.now()}

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)

        self.fields['date'].value = datetime.datetime.now()
        if self.instance:
            self.fields['date'].value = datetime.datetime.now()
            self.fields['category'].queryset = ContentCategory.objects.filter(usergenerated=True)

PhotoFormSet = inlineformset_factory(ContentItem, Photo, extra=1)




class ProfileForm(forms.ModelForm):


    """
    Profile Form. Composed of
    first_name,last_name,date_of_birth,gender
    """
    class Meta:
        model = Person
        fields = ('first_name', 'second_name', 'occupation', 'city', 'facebook',
                  'twitter', 'site', 'about', 'photo')



class InviteForm(forms.Form):
    email = forms.EmailField()

class InviteAdminForm(forms.Form):
    email = forms.EmailField()
    email.label = u'Е-mail'
    email.help_text = u'Адрес электронной почты. Обязательно.'
    person = forms.ModelChoiceField(Person.objects.all(),
        widget=autocomplete_light.ChoiceWidget('PersonAutocompleteModelTemplate'), required=False)
    person.label = u'Если человек уже публиковался на сайте'
    person.help_text = u'Начните вводить имя человека'

class LoginForm(forms.Form):
    email = forms.EmailField()

    password = forms.CharField(widget=forms.PasswordInput())


class SearchForm(forms.Form):
    person = forms.ModelChoiceField(Person.objects.all(),
        widget=autocomplete_light.ChoiceWidget('PersonAutocompleteModelTemplate'))
