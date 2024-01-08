from django.views.generic import TemplateView
from utils.environ import get_environ

class EnvironsTemplateView(TemplateView):
    extra_context = {'page_title': 'Environ'}
    template_name = 'environs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['environs'] = get_environ()
        return context
    