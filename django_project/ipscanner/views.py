from django.views.generic import TemplateView


class IpscannerTemplateView(TemplateView):
    extra_context = {'page_title': 'IP Scanner'}
    template_name = 'ipscanner/index.html'