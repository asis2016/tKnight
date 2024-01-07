from django.views.generic import TemplateView

from utils.whoami import get_whoami
from utils.boottime import get_bootime



class DashboardTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yo'] = get_bootime()
        return context
    
    template_name = 'dashboard/index.html'