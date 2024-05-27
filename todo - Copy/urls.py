from django.urls import path
from .views import TestTemplate

urlpatterns = [
    path('', TestTemplate.as_view(), name='test_template')
]