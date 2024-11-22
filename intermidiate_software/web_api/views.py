import json

from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view

from socket_server.server.main import process_command2, process_command3


@api_view(['POST'])
def send_command2_view(request):
    '''Sends a django signal causes a command2 sender function call'''

    data = process_command2()

    status = 'Success'
    if data.get('error', None) != None:
        status = 'Error'

    return HttpResponse(json.dumps({'status': status, 'data': data}))

@api_view(['POST'])
def send_command3_view(request):
    '''Sends a django signal causes a command3 sender function call'''
    
    data = process_command3()

    status = 'Success'
    if data.get('error', None) != None:
        status = 'Error'

    return HttpResponse(json.dumps({'status': status, 'data': data}))
