from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from utils.environ import get_environ

class EnvironsTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': _('environ'), 'display': 'd-none'}
    template_name = 'environs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['environs'] = get_environ()
        return context
    