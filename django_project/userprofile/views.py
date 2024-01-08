from django.views.generic import TemplateView


class UserProfileTemplateView(TemplateView):
    extra_context = {'page_title': 'My Profile'}
    template_name = 'userprofile/index.html'