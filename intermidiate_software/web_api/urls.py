from django.urls import path
from .views import send_command2_view, send_command3_view, get_clients_list_view, get_documentation


urlpatterns = [
    path('', get_clients_list_view),                # Clients list query
    path('c2/<int:address>', send_command2_view),   # Query to send command with packetType 2
    path('c3/<int:address>', send_command3_view),   # Query to send command with packetType 3
    path('doc/', get_documentation),                # Query to get REST API documentation
]
