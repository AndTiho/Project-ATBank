from typing import Any
import csv
import json

def csv_to_python_data(file_path: str) -> Any:
    """Функция принимает ПУТЬ к файлу CSV и преобразует его в Python список словарей,
    либо возвращает пустой Python список.
     Пример пути к файлу: './data/transactions.csv' """
    python_data = []
    try:
        with open(file_path, "r",  encoding="utf-8") as file:
            python_data = csv.DictReader(file, delimiter= ';')
            csv_list = list(python_data)
    except OSError:
        print("Ошибка декодирования файла, возвращаем пустой список.")
        return python_data
    except TypeError:
        print("Не верно указан путь. Возвращаем пустой список.")
        return python_data
    return csv_list

print(csv_to_python_data('./data/transactions.csv'))
