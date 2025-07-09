import re
from collections import Counter
# from csv_excel_utils import csv_to_python_data

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    if not isinstance(data, list):
        raise TypeError("Входные данные не являются списком")
    new_dict = []
    pattern = re.compile(search)
    for dict_data in data:
        if pattern.search(str(dict_data)):
            new_dict.append(dict_data)
    return new_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    if not isinstance(data, list):
        raise TypeError("Входные данные не являются списком")
    new_dict: dict = {}
    descriptions = [x.get("description") for x in data]
    counter = Counter(descriptions)
    for i in categories:
        result = counter[i]
        new_dict[i] = result
    return new_dict

# need_data = csv_to_python_data('./data/transactions.csv')
# need_data = []
# print(process_bank_operations(need_data, ["Открытие вклада"]))