from django.urls import path
from .views import traceroute_post_request, TraceRoutesFormView

urlpatterns = [
    path('post-request/', traceroute_post_request, name='traceroute-post-request'),
    path('', TraceRoutesFormView.as_view(), name='traceroute'),
]