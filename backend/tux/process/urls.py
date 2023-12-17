# process/urls.py

from django.urls import path
from .views import get_processes, get_environ

urlpatterns = [
    path('', get_processes, name='processes'),
    path('environ', get_environ, name='environ'),
]