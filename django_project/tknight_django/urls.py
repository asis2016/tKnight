from django.contrib import admin
from django.urls import path
from dashboard.views import (
    DashboardTemplateView
)
from disks.views import get_disk_usage_json_view
from environs.views import EnvironsTemplateView
from ipscanner.views import IpscannerTemplateView
from lsofs.views import LsofsTemplateView
from portscanner.views import PortScannerTemplateView
from processes.views import get_ps_json_view
from traceroutes.views import TraceRoutesTemplateView
from userprofile.views import UserProfileTemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    #disks
    path('disk-usage/', get_disk_usage_json_view, name='disk-usage'),
    #environs
    path('environs/', EnvironsTemplateView.as_view(), name='environs'),
    #ipscanner
    path('ipscanner/', IpscannerTemplateView.as_view(), name='ipscanner'),
    #lsofs
    path('lsof/', LsofsTemplateView.as_view(), name='lsof'),
    #portscanner
    path('portscanner/', PortScannerTemplateView.as_view(), name='portscanner'),
    #processes
    path('ps/', get_ps_json_view, name='ps'),
    #traceroutes
    path('traceroute/', TraceRoutesTemplateView.as_view(), name='traceroute'),
    #userprofile
    path('userprofile/', UserProfileTemplateView.as_view(), name='userprofile'),
    #dashboard
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
