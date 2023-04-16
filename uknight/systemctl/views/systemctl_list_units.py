import os
from django.views.generic import TemplateView
from django.conf import settings


class SystemctlView(TemplateView):
    """
    """
    template_name = "systemctl/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SystemctlView, self).get_context_data(*args, **kwargs)

        #
        systemctl_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "systemctl.out")
        with open(systemctl_file) as f:
            systemctl = f.read()
        
        context["systemctl"] = systemctl
        return context


