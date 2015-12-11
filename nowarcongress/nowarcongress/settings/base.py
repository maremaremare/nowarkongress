# -*- coding: utf-8 -*-
"""Common settings and globals."""

from os.path import abspath, basename, dirname, join, normpath
from sys import path


# PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Site domain name:
SITE_DOMAIN_NAME = 'nowarcongress.com'

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# END PATH CONFIGURATION

APPEND_SLASH = True
# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Asta', 'ksawie@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# END MANAGER CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

# END DATABASE CONFIGURATION
LOGGING_LOG_SQL = True
LOGGING_OUTPUT_ENABLED = True

# GENERAL CONFIGURATION

DATABASE_OPTIONS = {'charset': 'utf-8'}
DEFAULT_CHARSET = 'utf-8'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'nowarcongress.com'
]

PREPEND_WWW = False

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
   
)
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
# END GENERAL CONFIGURATION
LOCALE_PATHS = (
    join(SITE_ROOT, 'locale/'),
)
# END GENERAL CONFIGURATION


# MEDIA CONFIGURATION

MEDIA_URL = '/media/'

# END MEDIA CONFIGURATION


STATIC_URL = '/static/'

# See:
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',

)

# END STATIC FILE CONFIGURATION

# TEMPLATE CONFIGURATION
# See:
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'main.context.write_context',


)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
# END TEMPLATE CONFIGURATION


# MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'timelog.middleware.TimeLogMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'snippetscream.ProfileMiddleware',

    'django.middleware.cache.FetchFromCacheMiddleware',

    'htmlmin.middleware.MarkRequestMiddleware',



)
# END MIDDLEWARE CONFIGURATION


# URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
# END URL CONFIGURATION

SITE_ID = 1

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'social.apps.django_app.default',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'haystack',
    'inviter',
    'fluent_comments',
    'crispy_forms',
    #'debug_toolbar',
    #'debug_logging',
    
    'threadedcomments',
    'django.contrib.comments',
    'app_name_translation_in_admin',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

INVITER_FROM_EMAIL = 'admin@nowarcongress.com'
COMMENTS_APP = 'fluent_comments'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('email', 'url', 'title')
GRAPPELLI_INDEX_DASHBOARD = 'main.dashboard.CustomIndexDashboard'
FLUENT_COMMENTS_USE_EMAIL_NOTIFICATION = False
AKISMET_API_KEY = "381df759abfe"
AKISMET_IS_TEST = False                        # Enable to make test runs
# Enabled by default when AKISMET_API_KEY is set.
FLUENT_CONTENTS_USE_AKISMET = False
# Auto-close comments after N days
FLUENT_COMMENTS_CLOSE_AFTER_DAYS = None
# Auto-moderate comments after N days.
FLUENT_COMMENTS_MODERATE_AFTER_DAYS = None
FLUENT_COMMENTS_AKISMET_ACTION = 'moderate'    # Set to 'moderate' or 'delete'
PAGINATION_INVALID_PAGE_RAISES_404 = True

RECAPTCHA_PUBLIC_KEY = '6LfsAvYSAAAAAAynxBZRnV2IRphdGthNensF4mUa'
RECAPTCHA_USE_SSL = True
#CAPTCHA_AJAX = True


SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}


THIRD_PARTY_APPS = (
    'import_export', 'moderation', 'compressor', 'timelog', 'snippetscream', 'clear_cache', 'sitemetrics', 'django_extensions', 'sorl.thumbnail', 'newsletter',  'admin_utils', 'pagination', 'embed_video', 'south', 'ordered_model',  'mptt', 'django_mptt_admin',  'django_messages', 'captcha', 'taggit', 'taggit_templatetags', 'autocomplete_light',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'content', 'main', 'person',  'menu',  'media',  'events',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION


SOCIAL_AUTH_PIPELINE = (

    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.user.user_password'
    


)


AUTHENTICATION_BACKENDS = (

    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.email.EmailAuth',
    'django.contrib.auth.backends.ModelBackend',
)


FACEBOOK_APP_ID = '1423110517962392'

SOCIAL_AUTH_FACEBOOK_KEY = '1423110517962392'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '550137041096-eq4b7f38mkum06onojt7ep37ajoi9nec.apps.googleusercontent.com'

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/loginfailed/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/profile/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/profile/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/profile/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'
SOCIAL_AUTH_EMAIL_FORM_URL = '/login-form/'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'login_form.html'
LOGIN_URL = '/login-form/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'


import os
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'xapian_backend.XapianEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
    },
    'whoosh': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_XAPIAN_LANGUAGE = 'ru'

# LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

TIMELOG_LOG = os.path.join(SITE_ROOT, 'time.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',

        },

        'timelog': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': TIMELOG_LOG,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
       
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'my': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'loggers': {
            'timelog.middleware': {
                'handlers': ['timelog'],
                'level': 'DEBUG',
                'propagate': False,
            }
        }
    }
}


from django.utils.translation import ugettext_lazy as _

_(u'Auth')  # for auth app_name
_(u'Sites')
_(u'Content')
_(u'Main')
_(u'Events')
_(u'Media')
_(u'Menu')

# END LOGGING CONFIGURATION

#
# WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
# WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
# END WSGI CONFIGURATION

FILEBROWSER_DIRECTORY = 'photos/'
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

def grayscale(im):
    "Convert image to grayscale"
    if im.mode != "L":
        im = im.convert("L")
    return im

FILEBROWSER_VERSIONS =  {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'big_grayscale': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': '', 'methods': [grayscale]},
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

