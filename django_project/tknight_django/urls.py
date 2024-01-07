from django.contrib import admin
from django.urls import path
from dashboard.views import DashboardTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
