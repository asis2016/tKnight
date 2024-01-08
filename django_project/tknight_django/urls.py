from django.contrib import admin
from django.urls import path

from disks.views import get_disk_usage_json_view
from environs.views import EnvironsTemplateView
from ipscanner.views import IpscannerTemplateView
from lsofs.views import LsofsTemplateView
from portscanner.views import PortScannerTemplateView
from processes.views import get_ps_json_view, ProcessesTemplateView
from system_services.views import SystemctlServicesTemplateView
from traceroutes.views import TraceRoutesFormView, traceroute_post_request
from userprofile.views import UserProfileTemplateView

from dashboard.views import (
    DashboardTemplateView, WipTemplateView
)

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
    path('processes/', ProcessesTemplateView.as_view(), name='processes'),
    #system_services
    path('systemctl-services/', SystemctlServicesTemplateView.as_view(), name='systemctl-services'),
    #traceroutes
    path('traceroute/', TraceRoutesFormView.as_view(), name='traceroute'),
    path('traceroute-post-request/', traceroute_post_request, name='traceroute-post-request'),
    #userprofile
    path('userprofile/', UserProfileTemplateView.as_view(), name='userprofile'),
    #WIP
    path('wip/', WipTemplateView.as_view(), name='wip'),
    #dashboard
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
