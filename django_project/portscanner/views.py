from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PortScannerTemplateView(LoginRequiredMixin, TemplateView):
    extra_context = {'page_title': 'Port Scanner'}
    template_name = 'portscanner/index.html'