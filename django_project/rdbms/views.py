from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RdbmsManager

#utils
from utils.rdbms.tknight_mysql.schema import get_schemas
from utils.rdbms.tknight_mysql.database import get_database
from utils.rdbms.tknight_mysql.table import get_describe_table
from utils.rdbms.tknight_oracle.dba_users import get_dba_users


class RdbmsManagerCreateView(LoginRequiredMixin, CreateView):
    model = RdbmsManager
    extra_context = {
        'page_title': 'Add new RDBMS',
        'display': 'd-none'
    }
    template_name = 'rdbms/add.html'
    fields = '__all__'


class RdbmsManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = RdbmsManager
    extra_context = {'page_title': 'Update RDBMS', 'display': 'd-none'}
    template_name = 'rdbms/update.html'
    fields = '__all__'


class RdbmsManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = RdbmsManager
    template_name = 'rdbms/delete.html'
    extra_context = {'page_title': 'Delete RDBMS', 'display': 'd-none'}
    success_url = reverse_lazy('rdbms-manager-list')


class RdbmsManagerListView(LoginRequiredMixin, ListView):
    model = RdbmsManager
    extra_context = {'page_title': 'RDBMS Manager', 'display': 'd-none'}
    template_name = 'rdbms/index.html'


#Only for MySQL
class RdbmsMySQLManagerDetailView(LoginRequiredMixin, DetailView):
    model = RdbmsManager
    extra_context = {'page_title': 'All schemas', 'display': 'd-none'}
    template_name = 'mysql/detail.html'
    context_object_name = 'object'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        pk = self.kwargs['pk']
        obj_instance = RdbmsManager.objects.get(pk=pk)

        host = obj_instance.host
        username = obj_instance.username
        secret = obj_instance.password

        #run utils
        context['schemas'] = get_schemas(host, username, secret)
        return context
    

#Only for Oracle
class RdbmsOracleManagerDetailView(LoginRequiredMixin, DetailView):
    model = RdbmsManager
    extra_context = {'page_title': 'DBA Users', 'display': 'd-none'}
    template_name = 'oracle/dba-users.html'
    context_object_name = 'object'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        pk = self.kwargs['pk']
        obj_instance = RdbmsManager.objects.get(pk=pk)

        host = obj_instance.host
        username = obj_instance.username
        secret = obj_instance.password

        #run utils
        result = get_dba_users(USERNAME=username, SECRET=secret, DSN=host)
        context['dba_users'] = result
        return context


# todo > LoginRequiredMixin
@csrf_exempt
@require_POST
def mysql_show_schema_post_request(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        username = request.POST.get('username')
        secret = request.POST.get('password')
        db = request.POST.get('db')

        result = get_database(host, username, secret, db)
        
        return render(request, 'mysql/schemas.html', {
            'host':host,
            'username':username,
            'secret':secret,
            'db': db,
            'result': result,
            'page_title': 'MySQL Schema and it\'s tables',
            'display': 'd-none'
        })


# todo > LoginRequiredMixin
@csrf_exempt
@require_POST
def mysql_describe_table_post_request(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        username = request.POST.get('username')
        secret = request.POST.get('secret')
        db = request.POST.get('db')
        table_name = request.POST.get('table_name')
        result = get_describe_table(host, username, secret, db, table_name)
        
        return render(request, 'mysql/tables.html', {
            'result': result,
            'table_name': table_name,
            'page_title': 'MySQL table described', 
            'display': 'd-none'
        })
