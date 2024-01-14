from django.views.generic import TemplateView
from utils.profile import get_profile


class UserProfileTemplateView(TemplateView):
    extra_context = {'page_title': 'My Profile'}
    template_name = 'userprofile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
