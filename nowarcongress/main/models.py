# -*- coding: utf-8 -*-
from django.db import models
from ordered_model.models import OrderedModel
# ourapp.models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from content.models import ContentItem
from media.models import Photo
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


import logging

from filebrowser.fields import FileBrowseField
# Get an instance of a logger
logger = logging.getLogger('my')


class HomePageSection(OrderedModel):

    title = models.CharField(max_length=100, verbose_name=u'Название')
    limit = models.Q(app_label='content', model='topic') | models.Q(
        app_label='content', model='contentcategory')
    content_type = models.ForeignKey(ContentType, limit_choices_to=limit, verbose_name=u'Тип содержимого')
    object_id = models.PositiveIntegerField(verbose_name=u'ID содержимого')
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def itms(self):
  
        if self.content_type.model == 'contentcategory':
            return ContentItem.objects.filter(category__id=self.object_id)[:3]
        elif self.content_type.model == 'topic':
            return ContentItem.objects.filter(topic__id=self.object_id)[:3]

    class Meta(OrderedModel.Meta):
        verbose_name = ('Раздел главной страницы')
        verbose_name_plural = ('Разделы главной страницы')

    def __unicode__(self):
        return self.title


class SliderItem(OrderedModel):
    image = FileBrowseField("Image", max_length=200, directory="photos/", extensions=[".jpg",".jpeg",".png"], blank=True, null=True)
    item = models.ForeignKey(ContentItem, verbose_name=u'Материал')
    datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    slider_order = models.IntegerField(verbose_name=u'Порядок')

    class Meta(OrderedModel.Meta):
        verbose_name = ('Элемент слайдера')
        verbose_name_plural = ('Элементы слайдера')
        ordering = ['slider_order']

    def __unicode__(self):
        return self.item.title


# class ActualSlider(models.Model):
#     title = models.CharField(max_length=50, verbose_name=u'Название')
#     date = models.DateTimeField(auto_now=True)
#     items = models.ManyToManyField(SliderItem, verbose_name=u'Элементы')

#     class Meta:
#         verbose_name = ('Набор данных для слайдера')
#         verbose_name_plural = ('Данные для слайдера')

#     def related_items(self):
#         rc = SliderItem.objects.filter(parent_object_id=self.id)
#         result = []
#         for x in rc:
#             result.append(x)
#         return result

#     def __unicode__(self):
#         return self.title + ' ' + str(self.date)


class Partner(OrderedModel):
    title = models.CharField(max_length=100, verbose_name=u'Название')
    #icon = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(verbose_name=u'Cсылка')

    class Meta(OrderedModel.Meta):
        verbose_name = ('Партнер')
        verbose_name_plural = ('Партнеры')

    def __unicode__(self):
        return self.title


class Quote(models.Model):
    text = models.CharField(max_length=190, verbose_name=u'Текст цитаты')
    author_name = models.CharField(max_length=100, verbose_name=u'Имя автора')
    author_pic = FileBrowseField("Image", max_length=200, directory="photos/", extensions=[".jpg",".jpeg",".png"], blank=True, null=True)

    #author_pic = models.ImageField(upload_to='photos', verbose_name=u'Фото автора', null=True, blank=True) 

    full = models.ForeignKey(ContentItem, verbose_name=u'Связанный материал', null=True, blank=True)
    micro_thumbnail = ImageSpecField(source='author_pic',
                                    processors=[ResizeToFill(36, 36)],
                                    format='JPEG',
                                    options={'quality': 80})
    class Meta:
        verbose_name = ('Цитата для главной страницы')
        verbose_name_plural = ('Цитаты для главной страницы')

    def __unicode__(self):
        return self.author_name
