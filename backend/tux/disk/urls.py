# disk/urls.py

from django.urls import path
from .views import disk_usage, disk_partition

urlpatterns = [
    path('usage', disk_usage, name="disk-usage"),
    path('partition', disk_partition, name="disk-partition")
]