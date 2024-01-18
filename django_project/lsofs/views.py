from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from utils.lsof import get_lsof

class LsofsTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'LSOFs'}
    template_name = 'lsofs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lsofs'] = get_lsof()
        return context