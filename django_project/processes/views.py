from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.http import JsonResponse
from utils.ps import get_ps


class ProcessesTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': _('Processes')}
    template_name = 'processes/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['processes'] = get_ps()
        return context


def get_ps_json_view(request):
    '''
    Returns get_disk_usage() from utils as list of JSON objects.
    '''
    result = get_ps()
    return JsonResponse(result, safe=False)
