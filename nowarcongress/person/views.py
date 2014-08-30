# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView
from django.contrib.contenttypes.models import ContentType
from moderation.models import ModeratedObject
from django.http import HttpResponseRedirect
from .models import *
from main.models import SliderItem


# import User models and User forms
# from .forms import ProfileForm, BlogForm
from django.contrib.auth.models import User
from content.models import ContentItem, ContentCategory
from media.models import Photo, Video
from .mixins import LoginRequiredMixin
from itertools import chain
from .forms import *
from django.db.models import Q
from django import shortcuts
from django.db.models import Count
import datetime
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator




def navigation_autocomplete(request,
    template_name='nav_autocomplete.html'):

    q = request.GET.get('q', '')
    context = {'q': q}
    queries = {}
    queries['users'] = Person.objects.filter(
        Q(second_name__icontains=q)).distinct()[:5]
    context.update(queries)
    return shortcuts.render(request, template_name, context)




class PeopleListView(ListView):
    model = Person
    template_name = "people.html"

    # def get_queryset(self):
    #     return self.model.objects.annotate(num_items=Count('items')).order_by('-num_items')

    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['listtitle'] = u'Все члены конгресса'
        context['form'] = SearchForm

        return context

class PeopleInitiatorsListView(PeopleListView):

    # def get_queryset(self):
    #     return self.model.objects.filter(initial=True).annotate(num_items=Count('items')).order_by('-num_items')
    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['listtitle'] = u'Инициаторы конгресса'
        return context

class PeopleCommunityListView(PeopleListView):

    # def get_queryset(self):
    #     return self.model.objects.filter(initial=False).annotate(num_items=Count('items')).order_by('-num_items')
    def get_context_data(self, **kwargs):
        context = super(PeopleListView, self).get_context_data(**kwargs)
        context['listtitle'] = u'Сообщество конгресса'
        return context




class PersonDetailView(DetailView):
    model = Person
    template_name = "person.html"

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        contentitems = ContentItem.objects.filter(author=self.object)
        for x in contentitems:
            if not x.category.slug in context:
                context[x.category.slug] = []
            context[x.category.slug].append(x)
        return context

class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)

class PersonLogged(NeverCacheMixin, LoginRequiredMixin, TemplateView):
    template_name = "loggedin.html"

    def get_context_data(self, **kwargs):
        context = super(PersonLogged, self).get_context_data(**kwargs)
 
        post_list = ContentItem.objects.filter(
            author=self.request.user.profile)
        moderated_list = ContentItem.unmoderated_objects.filter(
            author=self.request.user.profile)
   
        context['blogposts'] = sorted(list(set(chain(post_list, moderated_list))), key=lambda instance: instance.date, reverse=True)
        return context


class ProfileUpdateView(NeverCacheMixin, LoginRequiredMixin, UpdateView):

    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,
    """
    model = Person
    form_class = ProfileForm
    template_name = "profileupdate.html"
    success_url = "/logged/"

    def get_queryset(self):
        base_qs = super(ProfileUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        By default this requires `self.queryset` and a `pk` or `slug` argument
        in the URLconf, but subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj

    def form_valid(self, form):
        if form.is_valid():

            form.instance.user = self.request.user
            form.instance.user.profile.save()
            super(ProfileUpdateView, self).form_valid(form)
            return HttpResponseRedirect('/profile/')

            
        else:
            return self.render_to_response(self.get_context_data(form=form(self.request.POST)))




class ContentUpdateView(LoginRequiredMixin, UpdateView):

    """
    Class that only allows authentic user to update their profile
    Composed of first_name,last_name,date_of_birth,gender,
    """
    model = ContentItem
    # form_class = ProfileForm
    template_name = "update.html"
    form_class = ContentForm

    # def get_queryset(self):
    #     base_qs = super(ContentUpdateView, self).get_queryset()
    #     return base_qs.filter(author=self.request.user.profile)

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        By default this requires `self.queryset` and a `pk` or `slug` argument
        in the URLconf, but subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        base_obj = super(ContentUpdateView, self).get_object()
        self.success_url = base_obj.get_absolute_url()
        if base_obj.author == self.request.user.profile:
            return base_obj
        else:
            raise PermissionDenied()

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(ContentUpdateView).form_valid(form)

    # def form_valid(self, form):
    #     form.instance.author = self.request.user.profile
    #     context = self.get_context_data()
    #     photo_form = PhotoFormSet(
    #         self.request.POST, self.request.FILES, instance=self.object)
    #     if photo_form.is_valid() and form.is_valid():
    #         self.object = form.save()
    #         photo_form.instance = self.object
    #         photo_form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=PhotoFormSet(self.request.POST, self.request.FILES)))

    # def get_context_data(self, **kwargs):
    #     context = super(ContentUpdateView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['formset'] = PhotoFormSet(
    #             self.request.POST, self.request.FILES, instance=self.object)

    #     else:
    #         context['formset'] = PhotoFormSet(instance=self.object)

    #     return context




class ContentCreateView(LoginRequiredMixin, CreateView):

    template_name = "create.html"
    success_url = "/profile/created/"
    # fields = ('category', 'title', 'text', 'topic', 'tags',
    # 'comments_enabled')
    model = ContentItem
    form_class = ContentForm

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super(ContentCreateView, self).get_initial()
        # Copy the dictionary so we don't accidentally change a mutable dict
        initial = initial.copy()
        initial['date'] = datetime.now().strftime('%Y-%m-%d')
           # etc...
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
    # form.instance.category = ContentCategory.objects.get(slug='blogs')
        return super(ContentCreateView, self).form_valid(form)

class BlogCreatedView(LoginRequiredMixin, TemplateView):

    template_name = "blogcreated.html"

    def get_context_data(self, **kwargs):
        context = super(BlogCreatedView, self).get_context_data(**kwargs)
        context['object'] = self.request.user.profile
        return context


class BlogListView(ListView):
    template_name = "genericlist.html"
    model = ContentItem

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['actualsidebar'] = SliderItem.objects.all()[:6]
        return context


from inviter.utils import invite
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from datetime import datetime
from django.forms.formsets import formset_factory

class InviteView(LoginRequiredMixin, TemplateView, FormView):

    form_class = InviteForm
    template_name = "invite.html"
    success_url = "/profile/invited"

    def form_valid(self, form):
        if form.is_valid():

            invite(form.cleaned_data['email'], self.request.user, current_time=datetime.now())

            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form(self.request.POST)))


    def get_context_data(self, **kwargs):
        context = super(InviteView, self).get_context_data(**kwargs)
        context['form'] = InviteForm

        return context



class InvitedView(LoginRequiredMixin, TemplateView):
    template_name = "invited.html"

class InviteAdminView(LoginRequiredMixin, TemplateView, FormView):

    form_class = InviteAdminForm
    template_name = "inviteadmin.html"
    success_url = "/siteadmin/admin/person/invited/"

    def form_valid(self, form):
        if form.is_valid():

            invite(form.cleaned_data['email'], self.request.user, profile=form.cleaned_data['person'], current_time=datetime.now())

            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form(self.request.POST)))


    def get_context_data(self, **kwargs):
        context = super(InviteAdminView, self).get_context_data(**kwargs)
        context['form'] = InviteAdminForm
        context['title'] = u'Послать приглашение'
        
        return context

class InvitedAdminView(LoginRequiredMixin, TemplateView):
    template_name = "invitedadmin.html"
    def get_context_data(self, **kwargs):
        context = super(InvitedAdminView, self).get_context_data(**kwargs)
        context['title'] = u'Приглашение отправлено'
        
        return context



class LoginView(TemplateView, FormView):
    form_class=LoginForm
    template_name = "login_form.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = LoginForm
        return context

