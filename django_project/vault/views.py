from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import VaultManager


class VaultManagerCreateView(CreateView):
    model = VaultManager
    extra_context = {'page_title': 'Add new credential'}
    template_name = 'vault/add.html'
    fields = '__all__'


class VaultManagerListView(ListView):
    model = VaultManager
    extra_context = {'page_title': 'Primary Vault'}
    template_name = 'vault/index.html'
    

class VaultManagerUpdateView(UpdateView):
    model = VaultManager
    extra_context = {'page_title': 'Update credential'}
    template_name = 'vault/update.html'
    fields = '__all__'
    

class VaultManagerDeleteView(DeleteView):
    model = VaultManager
    template_name = 'vault/delete.html'
    extra_context = {'page_title': 'Delete credential'}
    success_url = reverse_lazy('vault-manager-list')


class VaultManagerDetailView(DetailView):
    model = VaultManager
    extra_context = {'page_title': 'Credential detail'}
    template_name = 'vault/detail.html'
