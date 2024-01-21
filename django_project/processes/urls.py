from django.urls import path
from .views import ProcessesTemplateView, get_ps_json_view

urlpatterns = [
    path('json/', get_ps_json_view, name='json-ps'),
    path('', ProcessesTemplateView.as_view(), name='processes'),
]