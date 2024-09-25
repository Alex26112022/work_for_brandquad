from rest_framework.serializers import ModelSerializer

from nginx_logs.models import ParseLogs


class ParseLogsSerializer(ModelSerializer):
    """ Сериализатор для логов Nginx. """
    class Meta:
        model = ParseLogs
        fields = (
            'ip_address', 'date_log', 'method', 'uri', 'status_code', 'size')
