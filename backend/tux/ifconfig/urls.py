# ifconfig/urls.py

from django.urls import path
from .views import get_ifconfig

urlpatterns = [
    path('', get_ifconfig, name='ifconfig')
]