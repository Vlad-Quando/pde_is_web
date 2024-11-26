import json

from django.shortcuts import HttpResponse, render
from rest_framework.decorators import api_view

from socket_server.server.main import process_command2, process_command3, process_clients_list


@api_view(['GET'])
def send_command2_view(request, address):
    '''Sends a django signal causes a command2 sender function call'''

    data = process_command2(address)

    status = 'Success'
    if data.get('error', None) != None:
        status = 'Error'

    return HttpResponse(json.dumps({'status': status, 'data': data}))

@api_view(['GET'])
def send_command3_view(request, address):
    '''Sends a django signal causes a command3 sender function call'''
    
    data = process_command3(address)

    status = 'Success'
    if data.get('error', None) != None:
        status = 'Error'

    return HttpResponse(json.dumps({'status': status, 'data': data}))


@api_view(['GET'])
def get_clients_list_view(request):
    '''Returns a list of connected clients'''

    data = process_clients_list()
    status = 'Success'
    if data.get('error', None) != None:
        status = 'Error'

    return HttpResponse(json.dumps({'status': status, 'data': data}))


@api_view(['GET'])
def get_documentation(request):
    '''Returns a documentation on html-page'''

    return render(request, 'web_api/rest_api_doc.html')
