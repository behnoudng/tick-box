from django.urls import path
from .views import Home, CreateNewTask, UpdateTask

urlpatterns = [
    path('task/new/', CreateNewTask.as_view(), name='new_task'),
    path('task/<int:pk>/edit/', UpdateTask.as_view(), name='update_task'),
    path('', Home.as_view(), name='home'),
]