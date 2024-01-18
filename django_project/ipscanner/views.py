from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.http import JsonResponse
from utils.ip_scanner import get_ips
from utils.ifconfig import get_ifconfig

class IpscannerTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'IP Scanner'}
    template_name = 'ipscanner/index.html'


#todo > LoginRequiredMixin
@csrf_exempt
@require_POST
def ipscanner_post_request(request):
    if request.method == 'POST':
        start_ip = request.POST.get('start_ip')
        end_ip = request.POST.get('end_ip')
        result = get_ips(start_ip=start_ip, end_ip=end_ip)
        return render(request, 'ipscanner/result.html', {
            'result': result,
            'page_title': 'IP Scanner result'
        })


def get_ifconfig_as_json(request):
    '''
    Returns get_ifconfig() from utils.
    '''
    disk_usage = get_ifconfig()
    result = disk_usage['result']
    return JsonResponse(result, safe=False)
