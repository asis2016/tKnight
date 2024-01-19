from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

from disks.views import get_disk_usage_json_view
from environs.views import EnvironsTemplateView

from lsofs.views import LsofsTemplateView
from portscanner.views import PortScannerTemplateView
from processes.views import get_ps_json_view, ProcessesTemplateView
from traceroutes.views import TraceRoutesFormView, traceroute_post_request
from userprofile.views import UserProfileTemplateView

from system_services.views import (
    SystemctlServicesTemplateView,
    get_systemctl_services_json_view
)

from ipscanner.views import (
    IpscannerTemplateView,
    get_ifconfig_as_json,
    ipscanner_post_request
)

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
    #environs
    path('environs/', EnvironsTemplateView.as_view(), name='environs'),
    path('ipscanner-post-request/', ipscanner_post_request, name='ipscanner-post-request'),
    path('ipscanner/', IpscannerTemplateView.as_view(), name='ipscanner'),
    #lsofs
    path('lsof/', LsofsTemplateView.as_view(), name='lsof'),
    #portscanner
    path('portscanner/', PortScannerTemplateView.as_view(), name='portscanner'),
    path('processes/', ProcessesTemplateView.as_view(), name='processes'),
    #wip
    path('wip/', WipTemplateView.as_view(), name='wip'),
    #rdbms
    path('rdbms/', include('rdbms.urls')),
    #profile
    path('userprofile/', UserProfileTemplateView.as_view(), name='userprofile'),
    
    #dashboard
    #json_view
    path('json/ifconfig/', get_ifconfig_as_json, name='json-ifconfig'),
    path('json/ps/', get_ps_json_view, name='json-ps'),
    path('json/disk/usage/', get_disk_usage_json_view, name='json-disk-usage'),
    path('json/sensors/battery/', get_sensors_battery_json_view, name='json-sensors-battery'),
    path('json/systemctl/services/', get_systemctl_services_json_view, name='json-systemctl-services'),

    path('', DashboardTemplateView.as_view(), name='dashboard'),
    prefix_default_language=False,  # Do not include language prefix for the default language
)
