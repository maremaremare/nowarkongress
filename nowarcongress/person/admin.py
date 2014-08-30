from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from django.conf.urls import patterns, url
from admin_utils import make_admin_class
from person.views import *

make_admin_class("Invite", patterns("person.views",
    url(r'^$', InviteAdminView.as_view(), name='person_invite_changelist'),
), "person")

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PersonInline, )

# Re-register UserAdmin
from filebrowser.widgets import FileInput

class PhotoOptions(admin.ModelAdmin):
    list_display = ('__unicode__', 'occupation')
    formfield_overrides = {
        models.ImageField: {'widget': FileInput},
    }

admin.site.unregister(User)
admin.site.register(User, UserAdmin)





admin.site.register(Person, PhotoOptions)

