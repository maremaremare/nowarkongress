
from django.conf.urls import patterns, url
from .views import *
from content.views import AuthorListView
urlpatterns = patterns('person.views',

             

                       url(r'^$', PersonLogged.as_view()),

                       url(r'^settings/$', TemplateView.as_view(template_name="profile_settings.html")),


                       url(r'^update/$', ProfileUpdateView.as_view()),

                       url(
                           r'create/$',
                           ContentCreateView.as_view(),
                           name='blogcreate'
                       ),

                       url(
                           r'invite/$',
                           InviteView.as_view(),
                           name='invite'
                       ),

                       url(
                           r'invited/$',
                           InvitedView.as_view(),
                           name='invited'
                       ),

                       url(
                           r'created/$',
                           BlogCreatedView.as_view(),
                           name='blogcreated'
                       ),

                       url(
                           r'(?P<pk>\d+)/allcontent/$',
                           AuthorListView.as_view(),
                           name='authorlist'
                       ),

                       url(
                           r'^(?P<pk>\d+)/$',
                           PersonDetailView.as_view(),
                           name='detail'
                       ),



                       url(r'nav/$', 'navigation_autocomplete', name='navigation_autocomplete'),


                       )
