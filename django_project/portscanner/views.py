from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from utils.port_scanner import get_port_scanner


class PortScannerTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'Port Scanner'}
    template_name = 'portscanner/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hostname = self.request.GET.get('q', '')
        
        if hostname:
            context['hostname'] = hostname
            print('hostname')
            print(hostname)

            result = get_port_scanner(hostname)
            context['result'] = result
        
        return context
