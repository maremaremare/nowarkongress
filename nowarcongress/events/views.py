# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, View, CreateView
from django import forms
from .models import *
from content.models import Petition, OuterParticipant, ContentItem
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from captcha.fields import ReCaptchaField

class AddNameToPetitionView(SingleObjectMixin, View):
  
    model = Petition

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        # Look up the author we're interested in.
        self.object = self.get_object()
        # if not request.user.profile in self.object.participants.all():
        #     self.object.participants.add(request.user.profile)
        #     self.object.save()
        try:
            newsignature, created = OuterParticipant.objects.get_or_create(first_name=request.user.profile.first_name, second_name=request.user.profile.second_name, city=request.user.profile.city)
            
            self.object.outerparticipants.add(newsignature)
            self.object.save()
            if hasattr(self.request.session, 'signed_petitions'):
                self.request.session['signed_petitions'].append(int(self.object.id))
            else:
                self.request.session['signed_petitions'] = [int(self.object.id)]

            return HttpResponseRedirect('/petition/{0}'.format(self.object.contentitem.all()[0].id))

        except:
            raise


            return HttpResponseRedirect('/petition/{0}'.format(self.object.contentitem.all()[0].id))


class AddOuterNameToPetitionView(View):
    model = Petition
    def get(self, request, *args, **kwargs):

        # Look up the author we're interested in.
        petition = Petition.objects.get(id=kwargs['petition'])
        try:
            participant = OuterParticipant.objects.get(name=request.session['name'], city=request.session['city'], occupation=request.session['occupation'])
            petition.outerparticipants.add(participant)
            petition.save()

            x = self.request.session['signed_petitions']
            x.append(int(self.kwargs['petition']))
            self.request.session['signed_petitions'] = x
            return HttpResponseRedirect(request.GET['back'])
        except:
            
            return HttpResponseRedirect(request.GET['back'])




class ParticipantsView(DetailView):
    model = Petition
    template_name = 'list_petition_participants.html'

    def get_context_data(self, **kwargs):
        context = super(ParticipantsView, self).get_context_data(**kwargs)
        context['allpetitions'] = ContentItem.objects.filter(category__slug='petitions')[:5]
        return context


class OuterParticipantsForm(forms.ModelForm):
    #captcha = ReCaptchaField(label=u'Не робот ли Вы?')

    class Meta:
        model = OuterParticipant


class OuterParticipantsCreateView(CreateView):
    model = OuterParticipant
    template_name = 'outerpetitioncreate.html'
    #form_class = OuterParticipantsForm

    def __init__(self, **kwargs):
    # Go through keyword arguments, and either save their values to our
    # instance, or raise an error.
        self.kwargs = kwargs
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def form_valid(self, form):
        try:

            if form.is_valid():
                self.object = form.save()
                petition = Petition.objects.get(id=self.kwargs['petition'])
                petition.outerparticipants.add(self.object)
                petition.save() 

                self.request.session['signed_petitions'] = [int(self.kwargs['petition'])]
                self.request.session['first_name'] = form.cleaned_data['first_name']
                self.request.session['second_name'] = form.cleaned_data['second_name']
                self.request.session['city'] = form.cleaned_data['city']
                self.request.session['occupation'] = form.cleaned_data['occupation']

                return HttpResponseRedirect(petition.contentitem.all()[0].get_absolute_url())
            else:
                raise
        except:
            raise
    def get_context_data(self, **kwargs):
        context = super(OuterParticipantsCreateView, self).get_context_data(**kwargs)
        context['pk'] = kwargs
        return context
