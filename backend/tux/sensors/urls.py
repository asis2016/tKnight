# sensors/urls.py

from django.urls import path
from .views import sensors_temperature_view, sensors_battery_view, sensors_fans_view

urlpatterns = [
    path('temperature', sensors_temperature_view, name='sensor-temperature'),
    path('battery', sensors_battery_view, name='sensor-battery'),
    path('fans', sensors_fans_view, name='sensor-fans'),
]