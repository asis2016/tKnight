from django.views.generic import TemplateView


class LsofsTemplateView(TemplateView):
    extra_context = {'page_title': 'LSOFs'}
    template_name = 'lsofs/index.html'