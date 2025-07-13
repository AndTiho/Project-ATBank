import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция для поиска заданной строки в списке словарей"""
    if not isinstance(data, list):
        raise TypeError("Входные данные не являются списком")
    new_dict = []
    pattern = re.compile(search)
    for dict_data in data:
        if pattern.search(str(dict_data)):
            new_dict.append(dict_data)
    return new_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция для подсчёта данных в списке словарей по заданным категориям"""
    if not isinstance(data, list):
        raise TypeError("Входные данные не являются списком")
    new_dict: dict = {}
    descriptions = [x.get("description") for x in data]
    counter = Counter(descriptions)
    for i in categories:
        result = counter[i]
        new_dict[i] = result
    return new_dict
