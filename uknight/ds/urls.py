from django.urls import path
from .views import *

urlpatterns = [
    path('', DsView.as_view(), name="ds"),
]