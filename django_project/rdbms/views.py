from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RdbmsManager

#utils
from utils.rdbms.schema import get_schemas
from utils.rdbms.database import get_database


class RdbmsManagerCreateView(CreateView):
    model = RdbmsManager
    extra_context = {'page_title': 'Add new RDBMS'}
    template_name = 'rdbms/add.html'
    fields = '__all__'


class RdbmsManagerUpdateView(UpdateView):
    model = RdbmsManager
    extra_context = {'page_title': 'Update RDBMS'}
    template_name = 'rdbms/update.html'
    fields = '__all__'


class RdbmsManagerDeleteView(DeleteView):
    model = RdbmsManager
    template_name = 'rdbms/delete.html'
    extra_context = {'page_title': 'Delete RDBMS'}
    success_url = reverse_lazy('rdbms-manager-list')


class RdbmsManagerListView(ListView):
    model = RdbmsManager
    extra_context = {'page_title': 'RDBMS manager'}
    template_name = 'rdbms/index.html'


class RdbmsManagerDetailView(DetailView):
    model = RdbmsManager
    extra_context = {'page_title': 'RDBMS detail'}
    template_name = 'rdbms/detail.html'
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


@csrf_exempt
@require_POST
def mysql_db_post_request(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        username = request.POST.get('username')
        secret = request.POST.get('password')
        db = request.POST.get('db')

        result = get_database(host, username, secret, db)
        
        return render(request, 'mysql/databases.html', {
            'result': result,
            'page_title': 'MySQL Database'
        })

