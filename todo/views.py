from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Task


class Home(ListView):
    model = Task
    template_name = "home.html"


class CreateNewTask(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = ["title", "status"]
