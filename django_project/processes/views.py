from django.shortcuts import render
from django.http import JsonResponse
from utils.ps import get_ps


def get_ps_json_view(request):
    '''
    Returns get_disk_usage() from utils as list of JSON objects.
    '''
    result = get_ps()
    return JsonResponse(result, safe=False)
