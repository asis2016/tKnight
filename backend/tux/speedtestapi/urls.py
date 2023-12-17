# process/urls.py

from django.urls import path
from .views import get_speedtest

urlpatterns = [
    path('', get_speedtest, name='speed_test'),
]