import re
from collections import Counter, defaultdict


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    new_dict = []
    pattern = re.compile(search)
    for dict_data in data:
        if pattern.search(str(dict_data)):
            new_dict.append(dict_data)
    return new_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    new_dict: dict = defaultdict()
    descriptions = [x["description"] for x in data]
    counter = Counter(descriptions)
    for i in categories:
        result = counter[i]
        new_dict[i] = result
    return new_dict
