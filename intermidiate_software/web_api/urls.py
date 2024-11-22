from django.urls import path
from .views import send_command2_view, send_command3_view # , start_server, close_server


urlpatterns = [
    # path('start/', start_server),
    # path('close/', close_server),
    path('c2/', send_command2_view),
    path('c3/', send_command3_view),
]
