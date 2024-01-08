from django.views.generic import TemplateView


class TraceRoutesTemplateView(TemplateView):
    extra_context = {'page_title': 'Traceroute'}
    template_name = 'traceroutes/index.html'