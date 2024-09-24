from django.urls import path

from nginx_logs.apps import NginxLogsConfig
from nginx_logs.views import ParseLogsListAPIView

app_name = NginxLogsConfig.name

urlpatterns = [
    path('logs/', ParseLogsListAPIView.as_view(),
         name='logs_list')
]
