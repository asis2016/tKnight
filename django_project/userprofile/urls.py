from django.urls import path
from .views import UserProfileTemplateView

urlpatterns = [
    path('', UserProfileTemplateView.as_view(), name='userprofile'),
]