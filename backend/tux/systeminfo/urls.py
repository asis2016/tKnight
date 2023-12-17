# systeminfo/urls.py

from django.urls import path
from .views import sysinfo_boottime, sysinfo_users

urlpatterns = [
    path('boottime', sysinfo_boottime, name='sysinfo-boottime'),
    path('users', sysinfo_users, name='sysinfo-boottime'),
]