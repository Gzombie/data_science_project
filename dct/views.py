# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Student.settings")
django.setup()
from dct.models import student
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = 'interface.html'
    