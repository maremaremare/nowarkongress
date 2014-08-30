# -*- coding: utf-8 -*-
"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'nowarcongress.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = u'Конгресс интеллигенции против войны'

        self.children.append(modules.ModelList(
            (u'Контент'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('content.*', 'events.*', 'threadedcomments.*', 'taggit.*'),
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            (u'Пользователи'),
            column=1,
            collapsible=True,
            models=('django.contrib.auth.models.*', 'person.models.*',),
        ))

        self.children.append(modules.ModelList(
            (u'Главная страница'),
            column=1,
            collapsible=True,
            models=('main.models.HomePageSection', 'main.models.ActualSlider',
                    'main.models.SliderItem', 'menu.models.MenuItem', 'main.models.Quote', 'main.models.Partner'),
        ))
        self.children.append(modules.ModelList(
            (u'Фото и видео'),
            column=1,
            collapsible=True,
            models=('media.models.Photo', 'media.models.Video'),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            (u'Модерация'),
            column=2,
            children=[
                {
                    'title': (u'Смотреть очередь на модерацию'),
                    'url': 'http://nowarcongress.com/siteadmin/admin/moderation/moderatedobject/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            (u'Приглашения'),
            column=2,
            children=[
                {
                    'title': (u'Послать приглашение'),
                    'url': 'http://nowarcongress.com/siteadmin/admin/person/invite/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            (u'Статистика'),
            column=2,
            children=[
                {
                    'title': (u'Яндекс-метрика'),
                    'url': 'https://metrika.yandex.ru/stat/?counter_id=25557890',
                    'external': True,
                },
            ]
        ))

        self.children.append(modules.LinkList(
            (u'Рассылка'),
            column=2,
            children=[
                {
                    'title': (u'Рассылка'),
                    'url': 'http://nowarcongress.com/siteadmin/admin/newsletter/',
                    'external': False,
                },

               {
                    'title': (u'Вход в почтовый ящик'),
                    'url': 'https://mail.yandex.ru/for/nowarcongress.com/',
                    'external': True,
                },
            ]
        ))
        self.children.append(modules.LinkList(
            (u'Файлы'),
            column=2,
            children=[
                {
                    'title': (u'Все файлы и фотографии'),
                    'url': 'http://nowarcongress.com/siteadmin/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=2,
        ))
