from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from nginx_logs.models import ParseLogs


class ParseLogsTestCase(APITestCase):
    def setUp(self):
        self.parse_logs = ParseLogs.objects.create(ip_address='127.0.0.1',
                                                   date_log='2022-01-01 12:00:00',
                                                   method='GET',
                                                   uri='http://93.180.71.3/downloads/product_1',
                                                   status_code=200,
                                                   size=100)

    def test_get_logs(self):
        url = reverse('nginx_logs:logs_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = response.json()
        self.assertEqual(res['results'][0]['ip_address'], '127.0.0.1')
