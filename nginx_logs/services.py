import json

from my_config import path_nginx_logs


def parse_log_nginx(logs=path_nginx_logs) -> list[dict]:
    """ Парсит лог-файл и возвращает список словарей. """
    json_logs = []
    with open(logs, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            json_logs.append(json.loads(line.strip()))
    return json_logs
