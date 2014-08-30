from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.contenttypes.models import ContentType
from .models import *
from main.models import  SliderItem
from itertools import chain
from django.core.exceptions import PermissionDenied
from person.mixins import LoginRequiredMixin
from .forms import *
from django.http import HttpResponseRedirect

# Create your views here.

import logging


# Get an instance of a logger
logger = logging.getLogger('my')



class ContentItemListView(ListView):

    #model=ContentItem
    
    def get_queryset(self):
        self.category = ContentCategory.objects.get(slug = self.kwargs['slug'])
        return ContentItem.objects.filter(category=self.category)
    def get_template_names(self):
        return [self.category.list_template]
    def get_context_data(self, **kwargs):
        context = super(ContentItemListView, self).get_context_data(**kwargs)

        context['category'] = self.category
        
        for item in self.category.sidebar.all():
            logger.info(item)
            if item.content_type and item.object_id:
                if item.content_type.model == 'contentcategory': 
                    context[item.context_name] = item.content_object.items.all()
                
                else:
                    context[item.context_name] = item.content_object
            elif item.content_type and not item.object_id:
                context[item.context_name] = item.content_type.model_class().objects.all()[:item.number]


        return context

class SessionListView(DetailView):
    model=Event
    template_name='list_session.html'

    def get_context_data(self, **kwargs):
        context = super(SessionListView, self).get_context_data(**kwargs)
        context['object_list'] = self.object.contentitem.all()
        context['actualsidebar'] = SliderItem.objects.all()[:6]
        context['advs'] = ContentItem.objects.filter(category__slug='recommendations')[:1]
        return context


class TopicListView(ListView):

    model=ContentItem
    template_name = 'list_topic.html'
    
    def get_queryset(self):
        self.topic = Topic.objects.get(slug = self.kwargs['slug'])
        return ContentItem.objects.filter(topic=self.topic)
        
    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        if len(self.object_list) > 3:
            context['actualsidebar'] = SliderItem.objects.all()[:6]
        context['advs'] = ContentItem.objects.filter(category__slug='recommendations')[:1]
        return context


class AuthorListView(ListView):

    model=ContentItem
    template_name = 'list_author.html'
    
    def get_queryset(self):
        self.author = Person.objects.get(pk = self.kwargs['pk'])
        if self.request.user.is_authenticated() and self.request.user.profile == self.author:
            post_list = ContentItem.objects.filter(
            author=self.author)
            moderated_list = ContentItem.unmoderated_objects.filter(
            author=self.author)
   
            return sorted(list(set(chain(post_list, moderated_list))), key=lambda instance: instance.date, reverse=True)

        else:
            return ContentItem.objects.filter(author=self.author)
        
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['author'] = self.author
        if len(self.object_list) > 3:
            context['actualsidebar'] = SliderItem.objects.all()[:6]
        context['advs'] = ContentItem.objects.filter(category__slug='recommendations')[:1]
        return context




class ContentDetailView(DetailView):
    model = ContentItem
    #template_name = 'content_detail.html'
    def get_template_names(self):
        return [self.object.category.detail_template]

        
    def get_context_data(self, **kwargs):
        context = super(ContentDetailView, self).get_context_data(**kwargs)


        
        for item in self.object.category.sidebar.all():
            logger.info(item)
            if item.content_type and item.object_id:
                if item.content_type.model == 'contentcategory': 
                    context[item.context_name] = item.content_object.items.all()
                
                else:
                    context[item.context_name] = item.content_object
            elif item.content_type and not item.object_id:
                context[item.context_name] = item.content_type.model_class().objects.all()[:item.number]


        return context

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        By default this requires `self.queryset` and a `pk` or `slug` argument
        in the URLconf, but subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        base_obj = super(ContentDetailView, self).get_object()
        if base_obj.get_moderation_status() != 1:
            if self.request.user.is_authenticated() and base_obj.author == self.request.user.profile:
                return base_obj
            else:
                
                raise PermissionDenied()

                #return HttpResponseForbidden()

        else:
            return base_obj



from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy



class ContentUpdateView(LoginRequiredMixin, UpdateView):

    """

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
        if form.is_valid():
            self.object = form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

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
    success_url = "/people/created"
    # fields = ('category', 'title', 'text', 'topic', 'tags',
    # 'comments_enabled')
    model = ContentItem
    form_class = ContentForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
    # form.instance.category = ContentCategory.objects.get(slug='blogs')
        return super(ContentCreateView, self).form_valid(form)
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
    #     context = super(ContentCreateView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['formset'] = PhotoFormSet(
    #             self.request.POST, self.request.FILES, instance=self.object)

    #     else:
    #         context['formset'] = PhotoFormSet(instance=self.object)

    #     return context



class ContentDeleteView(DeleteView):
    
    model = ContentItem
    success_url ='/profile/'
    template_name='delete.html'

    # def get_object(self, queryset=None):
    #     """
    #     Returns the object the view is displaying.
    #     By default this requires `self.queryset` and a `pk` or `slug` argument
    #     in the URLconf, but subclasses can override this to return any object.
    #     """
    #     # Use a custom queryset if provided; this is required for subclasses
    #     # like DateDetailView
    #     base_obj = super(ContentDeleteView, self).get_object()
    #     if base_obj.author == self.request.user.profile:
    #         return base_obj
    #     else:
    #         raise PermissionDenied()
