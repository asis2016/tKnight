# traceroute/urls.py

from django.urls import path
from .views import post_traceroute

urlpatterns = [
    path('', post_traceroute, name='traceroute')
]