### Individual settings ###

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# don't forget / at the end. 
# Check media with e.g. 
# http://127.0.0.1:8000/media/photos/dr_25_slidermax_thumbnail.jpg
MEDIA_ROOT = '/mnt/private/sites/digitalocean/backups/domains/nowarcongress.com/media/'
#MEDIA_ROOT = os.path.join(SITE_ROOT, 'domains/nowarcongress.com/media/')

# filebrowser has access to this directory, 
# http://django-filebrowser.readthedocs.org/en/latest/settings.html
# leave empty to access all.
# FILEBROWSER_DIRECTORY = MEDIA_ROOT
# FILEBROWSER_DIRECTORY = ''

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # for Django newer than at least 1.6:
        # 'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nowarcongress',
        'USER': 'django_login',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': normpath(join(SITE_ROOT, 'default.db')),
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}
# END DATABASE CONFIGURATION

