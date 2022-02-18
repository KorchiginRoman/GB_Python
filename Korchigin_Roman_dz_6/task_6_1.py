"""Модуль pprint позволяет красиво отображать объекты Python.
При этом сохраняется структура объекта и отображение, которое выводит pprint,
            можно использовать для создания объекта.
 Модуль pprint входит в стандартную библиотеку Python. """
from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""

    remote_addr = line.split(" - - ")[0]
    res_and_path = line.split('"')[1]
    request_type = res_and_path.split()[0]
    requested_resource = res_and_path.split()[1]
    return (remote_addr, request_type,
            requested_resource)  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:  # передавайте данные в функцию и наполняйте список list_out кортежами
        list_out.append(get_parse_attrs(line))

pprint(list_out)
