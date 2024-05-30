from django.urls import path
from .views import Home, CreateNewTask

urlpatterns = [
    path('new/', CreateNewTask.as_view(), name='new_task'),
    path('', Home.as_view(), name='home'),
]