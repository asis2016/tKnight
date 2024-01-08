from django.views.generic import TemplateView


class PortScannerTemplateView(TemplateView):
    extra_context = {'page_title': 'Port Scanner'}
    template_name = 'portscanner/index.html'