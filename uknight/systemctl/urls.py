from django.urls import path
from .views import *

urlpatterns = [
    path('', SystemctlView.as_view(), name="systemctl_list_units"),
]