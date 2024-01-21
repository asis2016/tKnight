from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from disks.views import get_disk_usage_json_view
from environs.views import EnvironsTemplateView

from lsofs.views import LsofsTemplateView
from portscanner.views import PortScannerTemplateView

from dashboard.views import (
    DashboardTemplateView, 
    WipTemplateView,
    password_manager_logout,
    get_sensors_battery_json_view
)


###
from django.views.i18n import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', password_manager_logout, name='pm_logout'),
    
]

urlpatterns += i18n_patterns(
    path('systemctl-services/', include('system_services.urls')),
    path('traceroute/', include('traceroutes.urls')),
    path('ps/', include('processes.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('rdbms/', include('rdbms.urls')),
    path('ipscanner/', include('ipscanner.urls')),
    path('vault/', include('vault.urls')),
    
    #environs
    path('environs/', EnvironsTemplateView.as_view(), name='environs'),
    
    #lsofs
    path('lsof/', LsofsTemplateView.as_view(), name='lsof'),
    #portscanner
    path('portscanner', PortScannerTemplateView.as_view(), name='portscanner'),
    
    #wip
    path('wip/', WipTemplateView.as_view(), name='wip'),

    #dashboard
    #json_view
    path('json/disk/usage/', get_disk_usage_json_view, name='json-disk-usage'),
    path('json/sensors/battery/', get_sensors_battery_json_view, name='json-sensors-battery'),
    path('', DashboardTemplateView.as_view(), name='dashboard'),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=True,  # Do not include language prefix for the default language
)
