from django.urls import path
from .views import (
    IpscannerTemplateView,
    get_ifconfig_as_json,
    ipscanner_post_request
)

urlpatterns = [
    path('json/', get_ifconfig_as_json, name='json-ifconfig'),
    path('ipscanner-post-request/', ipscanner_post_request, name='ipscanner-post-request'),
    path('', IpscannerTemplateView.as_view(), name='ipscanner'),
]