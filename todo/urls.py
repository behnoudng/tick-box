from django.urls import path
from .views import Home, CreateNewTask, UpdateTask, DeleteTask, mark_done

urlpatterns = [
    path('task/new/', CreateNewTask.as_view(), name='new_task'),
    path('task/<int:pk>/edit/', UpdateTask.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name="del_task"),
    path('task/<int:pk>/mark_done', mark_done, name='mark_done'),
    path('', Home.as_view(), name='home'),
]