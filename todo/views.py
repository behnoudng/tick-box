from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task

class TestTemplate(ListView):
    model = Task
    template_name = 'home.html'
