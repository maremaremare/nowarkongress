# -*- coding: utf-8 -*-
"""Production settings and globals."""


from os import environ

from base import *

from secrets import *


INSTALLED_APPS += ('gunicorn',)
# HOST CONFIGURATION
# See:
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [SITE_DOMAIN_NAME]


# END HOST CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'admin@nowarcongress.com'
EMAIL_HOST_PASSWORD = EMAIL_PASS
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'ksawie@gmail.com'
# EMAIL_HOST_PASSWORD = 'tramontanazoom'


# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tl
# END EMAIL CONFIGURATION
STATICFILES_DIRS = (
    '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/static/',
)
STATIC_ROOT = '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/staticroot/'
MEDIA_ROOT = '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/media/'
COMPRESS_ROOT = '/home/maremare/domains/' + SITE_DOMAIN_NAME + '/static/'
COMPRESS_URL = '/static/'
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_DIRECTORY = 'photos/'
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
FILEBROWSER_VERSIONS =  {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': 'crop'},
    'slmax_thumbnail':  {'verbose_name': u'На верху статьи', 'width': 848, 'height': 350, 'opts': 'crop'},
    'slidermax_thumbnail':  {'verbose_name': u'slmax', 'width': 620, 'height': 350, 'opts': 'crop'},
    'slmin_thumbnail':  {'verbose_name': u'slmin', 'width': 96, 'height': 60, 'opts': ''},
    'sidebar_thumbnail':  {'verbose_name': u'sidebar', 'width': 50, 'height': 50, 'opts': 'crop'},
    'adv_thumbnail':  {'verbose_name': u'adv', 'width': 247, 'height': 175, 'opts': 'crop'},
    'adv_thumbnail_detail':  {'verbose_name': u'adv_detail', 'width': 247, 'height': '', 'opts': ''},
    'owlcarousel_thumbnail':  {'verbose_name': u'owlcarousel', 'width': 848, 'height': 485, 'opts': 'crop'},
    'list_thumbnail':  {'verbose_name': u'list', 'width': 340, 'height': 240, 'opts': 'crop'},
    'plist_thumbnail':  {'verbose_name': u'personlist', 'width': 200, 'height': 200, 'opts': 'crop'},
    'mini_thumbnail': {'verbose_name': u'mini', 'width': 50, 'height': 50, 'opts': 'crop'},
    'micro_thumbnail': {'verbose_name': u'micro', 'width': 25, 'height': 25, 'opts': 'crop'},
    'detail_thumbnail': {'verbose_name': u'owlcarousel', 'width': 100, 'height': 100, 'opts': 'crop'},
}

FILEBROWSER_ADMIN_VERSIONS = ['slmax_thumbnail', 'small', 'medium', 'big', 'large']

# DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nowarcongress',
        'USER': 'django_login',
        'PASSWORD': DB_PASS,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True
