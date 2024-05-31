from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task


class Home(ListView):
    model = Task
    template_name = "home.html"


class CreateNewTask(CreateView):
    model = Task
    template_name = "task_new.html"
    fields = ["title", "status"]


class UpdateTask(UpdateView):
    model = Task
    template_name = "task_edit.html"
    fields = ["title", "status"]

class DeleteTask(DeleteView):
    model = Task
    template_name = "task_del.html"
    success_url = reverse_lazy('home')


def mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = True
    task.save()
    return redirect('home')

