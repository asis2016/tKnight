from django.views.generic import TemplateView
from utils.systemctl_services import get_systemctl_services

class SystemctlServicesTemplateView(TemplateView):
    extra_context = {'page_title': 'Systemctl Services'}
    template_name = 'system_services/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['systemctl_services'] = get_systemctl_services()
        return context