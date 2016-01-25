from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from main.views import HomePageView
from moderation.helpers import auto_discover
auto_discover()
import autocomplete_light

autocomplete_light.autodiscover()
admin.autodiscover()

from django.http import HttpResponse
from person.views import *
from main.views import *
from content.views import *
from content.feed import LatestEntriesFeed
from events.views import *
from filebrowser.sites import site



def robots(request):
    html = 'User-agent: *\r\nDisallow: /siteadmin/admin'
    return HttpResponse(html)

def yandex(request):
    html = '48cf5d8bcfc1'
    return HttpResponse(html)

urlpatterns = patterns('',
                       url(r'^$',
                           cache_page(600)(HomePageView.as_view())),

                       # Examples:
                       # url(r'^$', 'nowarkongress.views.home', name='home'),
                       url(r'^0a0915f4dc4f.html', yandex),
                       url(r'^robots.txt', robots),
                       url(r'^feed/$', LatestEntriesFeed()),
                       url(r'^search/', SearchView.as_view()),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       url(r'^login-form/$', LoginView.as_view()),
                       url(r'^loginfailed/$', TemplateView.as_view(template_name='loginfailed.html')),
                       url(r'^signature/added/$', TemplateView.as_view(template_name='addedsignature.html')),
                       url(r'^comments/', include('fluent_comments.urls')),
                       url(r'^profile/messages/', include('django_messages.urls')),
                       url(r'^profile/', include('person.urls', namespace='people')),
                       url(r'^people/(?P<pk>\d+)/all/$', AuthorListView.as_view(), name='peoplecontentlist'),
                       url(r'^people/(?P<pk>\d+)/$', PersonDetailView.as_view(), name='peopledetail'),
                       url(r'^people/initiators/', PeopleInitiatorsListView.as_view()),
                       url(r'^people/community/', PeopleCommunityListView.as_view()),
                       url(r'^people/', PeopleListView.as_view()),

                       url(r'^tags/(?P<tag>[-\w]+)/', TagListView.as_view()),
                       url(r'^themes/(?P<slug>\w+)/', TopicListView.as_view()),
                       url(r'^about_congress/', MainAboutView.as_view()),
                       url(r'^petition/(?P<pk>\d+)/people/', cache_page(600)(ParticipantsView.as_view())),
                       url(r'^petition/(?P<pk>\d+)/addme/', AddNameToPetitionView.as_view()),

                       url(r'^petition/(?P<petition>\d+)/addouter/again/', AddOuterNameToPetitionView.as_view()),
                       url(r'^petition/(?P<petition>\d+)/addouter/', OuterParticipantsCreateView.as_view()),
                       url(r'^sessions/(?P<pk>\d+)/', SessionListView.as_view()),


                       url(r'^invites/', include('inviter.urls', namespace = 'inviter')),
                       url(r'^howtoregister/$', TemplateView.as_view(template_name='how.html')),
                       url(r'^newsletter/', include('newsletter.urls')),
                       url(r'^contacts/$', TemplateView.as_view(template_name='contacts.html')),

                       url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
                       url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
                       url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
                           # Example: /2012/nov/10/
                       

                       
                       url('', include('social.apps.django_app.urls', namespace='social')),

                       # (r'^facebook/', include('django_facebook.urls')),
                       # url(r'^captcha/', include('captcha.urls')),
                       url(r'autocomplete/', include('autocomplete_light.urls')),
                       url(r'^siteadmin/admin/filebrowser/', include(site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),

                       url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', ItemDayArchiveView.as_view(month_format='%m'),name="archive_day"),
                       url(r'^(?P<slug>\w+)/(?P<pk>\d+)/update/$', ContentUpdateView.as_view()),
                       url(r'^(?P<slug>\w+)/(?P<pk>\d+)/delete/$', ContentDeleteView.as_view()),
                       url(r'^(?P<slug>\w+)/(?P<pk>\d+)/$', ContentDetailView.as_view()),
                       url(r'^(?P<slug>\w+)/$', ContentItemListView.as_view()),
                       
                       url(r'^siteadmin/admin/person/invited/$', InvitedAdminView.as_view()),
                       url(r'^siteadmin/admin/', include('smuggler.urls')), # put it before admin url patterns
                       url(r'^siteadmin/admin/', include(admin.site.urls)),

                       )
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'',
                               include('django.contrib.staticfiles.urls')),
                           ) + urlpatterns
