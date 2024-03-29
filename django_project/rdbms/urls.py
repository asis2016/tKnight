from django.urls import path
from .views import (
    RdbmsMySQLManagerDetailView,
    RdbmsManagerUpdateView,
    RdbmsManagerDeleteView,
    RdbmsManagerCreateView,
    RdbmsManagerListView,
    #schema
    mysql_show_schema_post_request,
    mysql_describe_table_post_request
)

urlpatterns = [
    path('<int:pk>/', RdbmsMySQLManagerDetailView.as_view(), name='rdbms-mysql-manager-detail'),
    path('<int:pk>/edit/', RdbmsManagerUpdateView.as_view(), name='rdbms-manager-update'),
    path('<int:pk>/delete/', RdbmsManagerDeleteView.as_view(), name='rdbms-manager-delete'),
    path('create', RdbmsManagerCreateView.as_view(), name='rdbms-manager-add'),
    #mysql
    path('mysql/database/', mysql_show_schema_post_request, name='rdbms-mysql-database-list'),
    path('mysql/describe/table/', mysql_describe_table_post_request, name='rdbms-mysql-describe-table'),
    path('', RdbmsManagerListView.as_view(), name='rdbms-manager-list'),
]