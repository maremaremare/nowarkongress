# -*- coding: utf-8 -*-
from django.db import models
from person.models import Person

# Create your models here.



from content.models import ContentItem

class EventItem(models.Model):
    title = models.CharField(max_length=500)
    announcement = models.ForeignKey(ContentItem, related_name='an_event', null=True, blank=True, verbose_name=u'Название мероприятия')
    report = models.ForeignKey(ContentItem, related_name='rep_event', null=True, blank=True, verbose_name=u'Отчет по мероприятию')
    participants = models.ManyToManyField(Person, null=True, blank=True, verbose_name=u'Участники мероприятия')
    lectures = models.ManyToManyField(ContentItem, related_name='lec_event', null=True, blank=True, verbose_name=u'Доклады и речи с мероприятия')
    date = models.DateField()

    class Meta:
        verbose_name = ('Мероприятие')
        verbose_name_plural = ('Мероприятия')

    def __unicode__(self):
        return self.title

