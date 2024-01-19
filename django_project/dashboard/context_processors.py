from django.contrib.staticfiles.finders import find
from utils.ifconfig import get_ifconfig

def global_context(request):
    """
    Global context for all templates.
    """
    return {
        'ifconfig': get_ifconfig(),
    }
