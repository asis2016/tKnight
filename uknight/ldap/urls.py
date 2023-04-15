from django.urls import path
from .views import *

urlpatterns = [
    path('', LDAPView.as_view(), name="ldap"),
]