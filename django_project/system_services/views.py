from django.views.generic import TemplateView


class SystemctlServicesTemplateView(TemplateView):
    extra_context = {'page_title': 'Systemctl Services'}
    template_name = 'system_services/index.html'