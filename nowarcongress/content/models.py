# -*- coding: utf-8 -*-
from django.db import models
from person.models import Person
from taggit.models import RusTaggedItem
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from ordered_model.models import OrderedModel
from moderation.models import ModeratedObject



class DefaultSelectOrPrefetchManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self._select_related = kwargs.pop('select_related', None)
        self._prefetch_related = kwargs.pop('prefetch_related', None)

        super(DefaultSelectOrPrefetchManager, self).__init__(*args, **kwargs)

    def get_query_set(self, *args, **kwargs):
        qs = super(DefaultSelectOrPrefetchManager, self).get_query_set(*args, **kwargs)

        if self._select_related:
            qs = qs.select_related(*self._select_related)
        if self._prefetch_related:
            qs = qs.prefetch_related(*self._prefetch_related)

        return qs


# Create your models here.


class OuterParticipant(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=u'Имя')
    second_name = models.CharField(max_length=50, verbose_name=u'Фамилия')
    occupation = models.CharField(max_length=250, verbose_name=u'Род занятий', blank=True)
    city = models.CharField(max_length=50, verbose_name=u'Город', blank=True)

    class Meta:
        verbose_name = ('Человек, подписавший заявление')
        verbose_name_plural = ('Люди, подписавшие заявление')

    def __unicode__(self):
        return self.first_name+' '+self.second_name


class Petition(models.Model):
    title = models.CharField(max_length=300, verbose_name=u'Название заявления')
    #text = models.ForeignKey(ContentItem, related_name='petition', verbose_name=u'Заявление')
    #participants = models.ManyToManyField(Person, null=True, blank=True, related_name='petition', verbose_name=u'Подписавшие участники конгресса')
    outerparticipants = models.ManyToManyField(OuterParticipant, null=True, blank=True, related_name='petition', verbose_name=u'Сторонние подписавшие')
    date = models.DateField(auto_now_add=True)
    closed = models.BooleanField(verbose_name=u'Сбор подписей закрыт?', default=False)

    def people_form(self):
        if self.outerparticipants.count() > 9 and self.outerparticipants.count() < 15:
            return u''
        else:
            if self.outerparticipants.count() % 10 == 1 or self.outerparticipants.count() % 10 ==0 or self.outerparticipants.count() % 10 > 4:
                return u''
            elif self.outerparticipants.count() % 10 < 5:
                return u'a'


    def get_number(self):
        return  self.outerparticipants.count()

    def get_absolute_url(self):
        return '/petition/{0}/people'.format(self.id)


    class Meta:
        verbose_name = ('Заявление')
        verbose_name_plural = ('Заявления')

    def __unicode__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    class Meta:
        verbose_name = ('Cессия конгресса')
        verbose_name_plural = ('Сессии конгресса')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/sessions/{0}'.format(self.id)

class SidebarItem(OrderedModel):

    title = models.CharField(max_length=100, verbose_name=u'Название')
    template = models.CharField(max_length=100, verbose_name=u'Шаблон')
    limit = models.Q(app_label='content', model='contentitem') \
        | models.Q(app_label='content', model='topic') \
        | models.Q(app_label='content', model='contentcategory') \
        | models.Q(app_label='main', model='slideritem') \
        | models.Q(app_label='content', model='event')
    content_type = models.ForeignKey(
        ContentType, null=True, blank=True, limit_choices_to=limit, verbose_name=u'Тип контента')
    object_id = models.PositiveIntegerField(verbose_name=u'ID объекта', null=True, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    number = models.IntegerField(null=True, blank=True, verbose_name=u'Число объектов')
    context_name = models.CharField(null=True, blank=True, max_length=50, verbose_name=u'Имя для контекста')
    for_detail_only = models.BooleanField(verbose_name=u'Не показывать в списках')

    class Meta(OrderedModel.Meta):
        verbose_name = ('Элемент колонки')
        verbose_name_plural = ('Элементы колонки')

    def __unicode__(self):
        return self.title


class Topic(models.Model):

    title = models.CharField(max_length=100, verbose_name=u'Название')
    slug = models.SlugField(verbose_name=u'Имя для адресной строки', db_index=True)
    public = models.BooleanField()

    def get_absolute_url(self):
        return '/themes/{0}'.format(self.slug)

    class Meta:
        verbose_name = ('Тема')
        verbose_name_plural = ('Темы')

    def __unicode__(self):
        return self.title


class ContentCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Название')
    icon = models.CharField(max_length=50, verbose_name=u'Значок', help_text='Выберите значок <a href="http://fortawesome.github.io/Font-Awesome/icons/">здесь</a>, введите его название без fa-')
    item_template = models.CharField(max_length=100, verbose_name=u'Шаблон для объекта на главной странице')
    detail_template = models.CharField(max_length=100, verbose_name=u'Шаблон для страницы объекта' )
    list_template = models.CharField(max_length=100, verbose_name=u'Шаблон для списка объектов')
    sidebar = models.ManyToManyField(SidebarItem, null=True, blank=True, verbose_name=u'Что показывать в левой колонке')
    slug = models.SlugField(verbose_name=u'Имя для адресной строки', db_index=True)
    usergenerated = models.BooleanField(default=False, verbose_name=u'Могут ли пользователи сами создавать материалы с этой категорией?')

    def get_absolute_url(self):
        return '/{0}'.format(self.slug)

    class Meta:
        verbose_name = ('Категория материалов')
        verbose_name_plural = ('Категории материалов')

    def __unicode__(self):
        return self.title


class ContentItem(models.Model):

    title = models.CharField(max_length=200, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст')
    date = models.DateTimeField(auto_now=False, verbose_name=u'Дата')
    category = models.ForeignKey(
        ContentCategory, related_name='items', verbose_name=u'Категория', db_index=True)
    author = models.ForeignKey(
        Person, null=True, blank=True, related_name='items', verbose_name=u'Автор', db_index=True)
    source = models.URLField(null=True, blank=True, verbose_name=u'Ссылка')
    topic = models.ForeignKey(
        Topic, null=True, blank=True, related_name='items', verbose_name=u'Тема', db_index=True)
    tags = TaggableManager(
        through=RusTaggedItem, blank=True, verbose_name=u'Метки')
    comments_enabled = models.BooleanField(
        verbose_name=u'Разрешить комментирование')
    petition = models.ForeignKey(Petition, related_name='contentitem', null=True, blank=True, verbose_name=u'Заявление')
    event = models.ForeignKey(Event, related_name='contentitem', null=True, blank=True)
    #dateevent = models.DateField(auto_now=False, verbose_name=u'Дата мероприятия', null=True, blank=True)

    objects = DefaultSelectOrPrefetchManager(select_related=('category','author','topic',))

    def get_moderation_status(self):
        status = ModeratedObject.objects.get(
            object_pk=self.id, content_type__id=47).moderation_status
        return status

    def get_moderation_text(self):
        statuslist = [u'Отклонено', u'Принято', u'В очереди на модерацию']
        return statuslist[self.get_moderation_status()]
    get_moderation_text.short_description = u'Статус модерации'

    def get_absolute_url(self):
        return '/{0}/{1}'.format(self.category.slug, self.id)

    class Meta:
        verbose_name = ('Материал')
        verbose_name_plural = ('Материалы')
        ordering = ['-date']

    def __unicode__(self):
        return self.category.title + ': ' + self.title

from import_export import resources


class PetitionResource(resources.ModelResource):

    class Meta:
        model = Petition



class SignatureResource(resources.ModelResource):

    class Meta:
        model = OuterParticipant
        exclude = ('id', )


# django_monitor.nq(
#     model, [rel_fields = [], can_delete_approved = True,
#     manager_name = 'objects', status_name = 'status',
#     monitor_name = 'monitor_entry', base_manager = None]
# )

# import django_monitor
# Your model here
# django_monitor.nq(ContentItem)

# import gatekeeper

# gatekeeper.register(ContentItem)
