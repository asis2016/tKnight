from django.urls import path
from .views import *

urlpatterns = [
    path('identities', IdentitiesListView.as_view(), name="ds_identities"),
    path('settings', DSSettingsView.as_view(), name="ds_settings"),
    path('', DSListView.as_view(), name="ds"),
]