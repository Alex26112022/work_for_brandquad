from datetime import datetime
from django.core.management import BaseCommand

from nginx_logs.models import ParseLogs
from nginx_logs.services import parse_log_nginx


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Создает объекты-логи. """
        logs = parse_log_nginx()

        parse_logs_for_create = []

        for log in logs:
            time_ = log.get('time')
            date_object = datetime.strptime(time_, "%d/%b/%Y:%H:%M:%S %z")
            date_object_str = date_object.strftime('%Y-%m-%d %H:%M:%S %z')

            parse_logs_for_create.append(
                ParseLogs(
                    ip_address=log.get('remote_ip'),
                    date_log=date_object_str,
                    method=log.get('request').split()[0],
                    url=log.get('request').split()[1],
                    status_code=log.get('response'),
                    size=log.get('bytes')
                )
            )

        ParseLogs.objects.bulk_create(parse_logs_for_create)
        print('Логи добавлены!')
