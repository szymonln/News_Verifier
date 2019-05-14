from django import forms
from django.forms import ModelForm, formset_factory
from django.db import models
from .models import *


class NewsProviderForm(ModelForm):
    class Meta:
        model = NewsProvider
        fields = ['name', 'url']
        labels = {'name': '', 'url':''}

NewsProviderFormSet = formset_factory(NewsProviderForm, extra=1)
