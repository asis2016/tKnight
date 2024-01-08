from django.views.generic import TemplateView


class EnvironsTemplateView(TemplateView):
    extra_context = {'page_title': 'Environ'}
    template_name = 'environs/index.html'