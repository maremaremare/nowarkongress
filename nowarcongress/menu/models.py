# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


class MenuItem(MPTTModel):
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')
    title = models.CharField(max_length=100, verbose_name=u'Название')
    subtitle = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=u'Подзаголовок')
    path = models.CharField(
        max_length=200, null=True, blank=True, verbose_name=u'Ссылка')
    limit = models.Q(app_label='content', model='topic') | models.Q(
        app_label='content', model='contentcategory')
    content_type = models.ForeignKey(
        ContentType, limit_choices_to=limit, null=True, blank=True, verbose_name=u'Тип содержания')
    object_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=u'ID объекта')
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    order = models.IntegerField(blank=True, default=0, verbose_name=u'Порядок')

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        verbose_name = ('Элемент главного меню')
        verbose_name_plural = ('Элементы главного меню')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = 0
        super(MenuItem, self).save(*args, **kwargs)
