from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import VaultManager


class VaultManagerCreateView(LoginRequiredMixin, CreateView):
    model = VaultManager
    extra_context = {'page_title': _('Add new credential'), 'display': 'd-none'}
    template_name = 'vault/add.html'
    fields = '__all__'


class VaultManagerListView(LoginRequiredMixin, ListView):
    model = VaultManager
    extra_context = {'page_title': _('Primary Vault'), 'display': 'd-none'}
    template_name = 'vault/index.html'
    

class VaultManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = VaultManager
    extra_context = {'page_title': _('Update Credential'), 'display': 'd-none'}
    template_name = 'vault/update.html'
    fields = '__all__'
    

class VaultManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = VaultManager
    template_name = 'vault/delete.html'
    extra_context = {'page_title': _('Delete credential'), 'display': 'd-none'}
    success_url = reverse_lazy('vault-manager-list')


class VaultManagerDetailView(LoginRequiredMixin, DetailView):
    model = VaultManager
    extra_context = {'page_title': _('Credential Detail'), 'display': 'd-none'}
    template_name = 'vault/detail.html'
