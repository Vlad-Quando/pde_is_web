from django.urls import path
from .views import send_command2_view, send_command3_view, get_clients_list_view, get_documentation


urlpatterns = [
    path('', get_clients_list_view),
    path('c2/<int:address>', send_command2_view),
    path('c3/<int:address>', send_command3_view),
    path('doc/', get_documentation),
]
