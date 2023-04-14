from django.urls import path
from .views import *

urlpatterns = [
    path("dpkg", DpkgView.as_view(), name="dpkg"),
    path("", DashboardView.as_view(), name="home")
]