from django.db import models

options = {'blank': True, 'null': True}


class ParseLogs(models.Model):
    """ Модель логов парсинга. """
    ip_address = models.CharField(max_length=100, verbose_name='IP-адрес',
                                  **options)
    date_log = models.DateTimeField(verbose_name='Дата лога', **options)
    method = models.CharField(max_length=100, verbose_name='HTTP метод',
                              **options)
    uri = models.CharField(max_length=200, verbose_name='URI', **options)
    status_code = models.IntegerField(verbose_name='HTTP статус код',
                                      **options)
    size = models.IntegerField(verbose_name='Размер ответа', **options)

    def __str__(self):
        return f'Лог для {self.ip_address}'

    class Meta:
        verbose_name = 'Лог парсинга'
        verbose_name_plural = 'Логи парсинга'
