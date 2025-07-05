from typing import Any
import csv
import pandas as pd

def csv_to_python_data(file_path: str) -> Any:
    """Функция принимает ПУТЬ к файлу CSV и преобразует его в Python список словарей,
    либо возвращает пустой Python список.
     Пример пути к файлу: './data/transactions.csv' """

    if not isinstance(file_path, str):
        print("'Путь к файлу' должен быть строкой. Возвращаем пустой список.")
        return []
    try:
        with open(file_path, "r",  encoding="utf-8") as file:
            python_data = csv.DictReader(file, delimiter= ';')
            csv_list = list(python_data)
    except OSError:
        print("Ошибка декодирования файла, возвращаем пустой список.")
        return []
    except TypeError:
        print("Не верно указан путь. Возвращаем пустой список.")
        return []
    return csv_list


def excel_to_python_data(file_path: str) -> Any:
    """Функция принимает ПУТЬ к файлу CSV и преобразует его в Python список словарей,
    либо возвращает пустой Python список.
     Пример пути к файлу: './data/transactions_excel.xlsx' """

    if not isinstance(file_path, str):
        print("'Путь к файлу' должен быть строкой. Возвращаем пустой список.")
        return []
    try:
        df = pd.read_excel(file_path)
        excel_data = df.to_dict('records')
    except ValueError:
        print("Не верно указан путь. Возвращаем пустой список.")
        return []
    except OSError:
        print("Ошибка декодирования файла, возвращаем пустой список.")
        return []
    except UnboundLocalError:
        print("Не верно указан путь. Возвращаем пустой список.")
        return []
    return list(excel_data)
