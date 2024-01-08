from django.shortcuts import render
from django.http import JsonResponse
from utils.disk_usage import get_disk_usage


def get_disk_usage_json_view(request):
    '''
    Returns get_disk_usage() from utils as list of JSON objects.
    '''
    disk_usage = get_disk_usage()
    result = disk_usage['result']
    return JsonResponse(result, safe=False)
