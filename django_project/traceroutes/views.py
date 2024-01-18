from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from utils.traceroute import get_traceroute


class TraceRoutesFormView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'Traceroute'}
    template_name = 'traceroutes/index.html'


# todo > LoginRequiredMixin
@csrf_exempt
@require_POST
def traceroute_post_request(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        result = get_traceroute(hostname=hostname)

        return render(request, 'traceroutes/result.html', {
            'hostname': hostname,
            'result': result,
            'page_title': 'Traceroute result'
        })
