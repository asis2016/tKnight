from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from utils.port_scanner import get_port_scanner


class PortScannerTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {
                'page_title': _('Port Scanner'),
                'display': 'd-none'
                }
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
