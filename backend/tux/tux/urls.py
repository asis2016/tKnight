from django.contrib import admin
from django.urls import path, include
from whoami.views import get_whoami

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/disks/', include('disk.urls')),
    path('api/v1/ifconfig/', include('ifconfig.urls')),
    path('api/v1/sensors/', include('sensors.urls')),
    path('api/v1/sysinfo/', include('systeminfo.urls')),
    path('api/v1/traceroute/', include('traceroute.urls')),
    path('api/v1/speedtestapi/', include('speedtestapi.urls')),
    path('api/v1/processes/', include('process.urls')),

    path('api/v1/whoami/', get_whoami)
]
