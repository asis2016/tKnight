import os
from django.views.generic import TemplateView
from django.conf import settings
import subprocess


class DpkgView(TemplateView):
    template_name = "dpkg.html"
    

    def get_context_data(self, *args, **kwargs):
        context = super(DpkgView, self).get_context_data(*args, **kwargs)
        dpkg_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "dpkg.out")

        with open(dpkg_file) as file:
            context["dpkg"] = file.read()
        return context
