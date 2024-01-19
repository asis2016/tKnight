from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from utils.systemctl_services import get_systemctl_services
from django.http import JsonResponse

class SystemctlServicesTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'Systemctl Services'}
    template_name = 'system_services/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['systemctl_services'] = get_systemctl_services()
        return context
    

def get_systemctl_services_json_view(request):
    '''
    Returns get_disk_usage() from utils as list of JSON objects.
    '''
    result = get_systemctl_services()
    return JsonResponse(result, safe=False)