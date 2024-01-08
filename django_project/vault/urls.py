from django.urls import path
from .views import (
    VaultManagerDetailView,
    VaultManagerUpdateView,
    VaultManagerDeleteView,
    VaultManagerCreateView,
    VaultManagerListView
)

urlpatterns = [
    path('<int:pk>/', VaultManagerDetailView.as_view(), name='vault-manager-detail'),
    path('<int:pk>/edit/', VaultManagerUpdateView.as_view(), name='vault-manager-update'),
    path('<int:pk>/delete/', VaultManagerDeleteView.as_view(), name='vault-manager-delete'),
    path('create', VaultManagerCreateView.as_view(), name='vault-manager-add'),
    path('', VaultManagerListView.as_view(), name='vault-manager-list'),
]