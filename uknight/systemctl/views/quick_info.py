import os
import json
from django.conf import settings


def quick_systemctl_info():
    """
    """
    json_file = os.path.join(settings.SHELL_SCRIPT_DIRS, "top_services.json")
    with open(json_file) as f:
        data = json.load(f)
    return data