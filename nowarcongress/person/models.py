# -*- coding: utf-8 -*-
from django.db import models
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from taggit.models import RusTaggedItem
from taggit.managers import TaggableManager

from filebrowser.fields import FileBrowseField
from filebrowser.base import FileObject

class Person(models.Model):
    first_name =  models.CharField(max_length=200, verbose_name=u'Имя', null=True)
    second_name =  models.CharField(max_length=200, verbose_name=u'Фамилия', null=True)
    user = models.OneToOneField(User, blank=True, null=True, related_name='profile')
    #name = models.CharField(max_length=200, verbose_name=u'Имяифамилия')
    occupation = models.CharField(max_length=100, null=True, verbose_name=u'Род деятельности')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'Город')
    about = models.TextField(verbose_name=u'О себе', null=True)
    #email = models.EmailField(verbose_name=u'Email', blank=True, null=True)
    site = models.URLField(null=True, blank=True, verbose_name=u'Адрес сайта')
    facebook = models.URLField(null=True, blank=True, verbose_name=u'Фейсбук')
    twitter = models.URLField(null=True, blank=True, verbose_name=u'Твиттер')
    initial = models.BooleanField(verbose_name=u'Инициатор?', default=False)
    active = models.BooleanField(verbose_name=u'Опубликовать профиль на сайте, сделать доступными сообщения', default=False)
    #subscribed = models.BooleanField()
    photo  = models.ImageField(upload_to="photos/portraits/", null=True)

    def image(self):
        if self.photo:
            return FileObject(self.photo.path)
        return None
    #FileBrowseField("Image", max_length=200, directory="person/photos/", extensions=[".jpg",".jpeg",".png"], blank=True, null=True)
    # list_thumbnail = ImageSpecField(source='photo',
    #                                 processors=[ResizeToFill(200, 200)],
    #                                 format='JPEG',
    #                                 options={'quality': 90})
    # mini_thumbnail = ImageSpecField(source='photo',
    #                                 processors=[ResizeToFill(50, 50)],
    #                                 format='JPEG',
    #                                 options={'quality': 90})
    # micro_thumbnail = ImageSpecField(source='photo',
    #                                 processors=[ResizeToFill(25, 25)],
    #                                 format='JPEG',
    #                                 options={'quality': 90})
    # detail_thumbnail = ImageSpecField(source='photo',
    #                                 processors=[ResizeToFill(100, 100)],
    #                                 format='JPEG',
    #                                 options={'quality': 90})



    def name(self):
        return self.first_name+' '+self.second_name

    
    def get_absolute_url(self):
        return '/people/{0}/all/'.format(self.id)

    class Meta:
        verbose_name = ('Участник конгресса')
        verbose_name_plural = ('Участники конгресса')
        ordering = ['second_name']

    def __unicode__(self):
        if self.second_name:
            return self.name()
        else:
            return u'Приглашенный участник'



# from django.db.models import signals
# from news.models import create_stream_item
# signals.post_save.connect(create_stream_item, sender=BlogPost)
