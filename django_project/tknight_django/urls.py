from django.contrib import admin
from django.urls import path
from dashboard.views import (
    DashboardTemplateView, 
    get_disk_usage_json_view,
    get_ps_json_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('disk-usage/', get_disk_usage_json_view, name='disk-usage'),
    path('ps/', get_ps_json_view, name='ps'),
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
