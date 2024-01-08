from django.urls import path
from .views import (
    RdbmsManagerDetailView,
    RdbmsManagerUpdateView,
    RdbmsManagerDeleteView,
    RdbmsManagerCreateView,
    RdbmsManagerListView,
    #schema
    mysql_db_post_request
)

urlpatterns = [
    path('<int:pk>/', RdbmsManagerDetailView.as_view(), name='rdbms-manager-detail'),
    path('<int:pk>/edit/', RdbmsManagerUpdateView.as_view(), name='rdbms-manager-update'),
    path('<int:pk>/delete/', RdbmsManagerDeleteView.as_view(), name='rdbms-manager-delete'),
    path('create', RdbmsManagerCreateView.as_view(), name='rdbms-manager-add'),
    #mysql
    path('mysql/database/', mysql_db_post_request, name='rdbms-mysql-database-list'),
    path('', RdbmsManagerListView.as_view(), name='rdbms-manager-list'),
]