from rest_framework import filters
from rest_framework.generics import ListAPIView

from nginx_logs.models import ParseLogs
from nginx_logs.paginators import MyPaginator
from nginx_logs.serializers import ParseLogsSerializer


class ParseLogsListAPIView(ListAPIView):
    """ Возвращает список логов. """
    queryset = ParseLogs.objects.all()
    serializer_class = ParseLogsSerializer
    pagination_class = MyPaginator
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['method', 'status_code']
    search_fields = ['ip_address', 'method', 'status_code']
