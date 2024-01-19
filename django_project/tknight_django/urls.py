from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

from disks.views import get_disk_usage_json_view
from environs.views import EnvironsTemplateView
from ipscanner.views import (
    IpscannerTemplateView,
    get_ifconfig_as_json,
    ipscanner_post_request
)
from lsofs.views import LsofsTemplateView
from portscanner.views import PortScannerTemplateView
from processes.views import get_ps_json_view, ProcessesTemplateView
from system_services.views import SystemctlServicesTemplateView
from traceroutes.views import TraceRoutesFormView, traceroute_post_request
from userprofile.views import UserProfileTemplateView

from dashboard.views import (
    DashboardTemplateView, 
    WipTemplateView,
    password_manager_logout,
    get_sensors_battery_json_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', password_manager_logout, name='pm_logout'),
]

urlpatterns += i18n_patterns(
    #system_services
    path('systemctl-services/', SystemctlServicesTemplateView.as_view(), name='systemctl-services'),
    #traceroutes
    path('traceroute/', TraceRoutesFormView.as_view(), name='traceroute'),
    path('traceroute-post-request/', traceroute_post_request, name='traceroute-post-request'),
    #vault
    path('vault/', include('vault.urls')),
    #disks
    path('disk-usage/', get_disk_usage_json_view, name='disk-usage'),
    #environs
    path('environs/', EnvironsTemplateView.as_view(), name='environs'),
    #ipscanner
    path('ifconfig/', get_ifconfig_as_json, name='ifconfig'),
    path('ipscanner-post-request/', ipscanner_post_request, name='ipscanner-post-request'),
    path('ipscanner/', IpscannerTemplateView.as_view(), name='ipscanner'),
    #lsofs
    path('lsof/', LsofsTemplateView.as_view(), name='lsof'),
    #portscanner
    path('portscanner/', PortScannerTemplateView.as_view(), name='portscanner'),
    #ps
    path('ps/', get_ps_json_view, name='ps'),
    path('processes/', ProcessesTemplateView.as_view(), name='processes'),
    #wip
    path('wip/', WipTemplateView.as_view(), name='wip'),
    #rdbms
    path('rdbms/', include('rdbms.urls')),
    #profile
    path('userprofile/', UserProfileTemplateView.as_view(), name='userprofile'),
    #sensors
    path('sensors/battery/', get_sensors_battery_json_view, name='ps'),
    
    #dashboard
    path('', DashboardTemplateView.as_view(), name='dashboard'),
    prefix_default_language=False,  # Do not include language prefix for the default language
)
