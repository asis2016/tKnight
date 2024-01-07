from django.views.generic import TemplateView

from utils.whoami import get_whoami


class DashboardTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yo'] = get_whoami()
        return context
    
    template_name = 'dashboard/index.html'