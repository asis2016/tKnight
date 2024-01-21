from django.urls import path
from .views import SystemctlServicesTemplateView, get_systemctl_services_json_view

urlpatterns = [
    path('json/', get_systemctl_services_json_view, name='json-systemctl-services'),
    path('', SystemctlServicesTemplateView.as_view(), name='systemctl-services'),
]