from django.shortcuts import render
from django.views.generic import TemplateView

class TestTemplate(TemplateView):
    template_name = 'home.html'
