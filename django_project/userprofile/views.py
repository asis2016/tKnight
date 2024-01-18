from django.views.generic import TemplateView
from utils.profile import get_profile
from django.utils.translation import gettext as _


class UserProfileTemplateView(TemplateView):
    extra_context = {'page_title': _('My Profile')}
    template_name = 'userprofile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
