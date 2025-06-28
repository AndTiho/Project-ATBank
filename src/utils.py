import json


def json_to_python_data(file_path: str) -> list:
    """Функция принимает ПУТЬ к файлу JSON и преобразует его в Python список,
    либо возвращает пустой Python список.
     Пример пути к файлу: '../data/operations.json' """
    python_data = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                python_data = json.load(file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла, возвращаем пустой список")
                return python_data
    except TypeError:
        print("Не верно указан путь")
        return python_data
    except FileNotFoundError:
        print("Файл не найден, возвращаем пустой список")
        return python_data
    return python_data

