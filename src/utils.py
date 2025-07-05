import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w",
    encoding="utf-8",
)

json_to_python_logger = logging.getLogger("app.utils_json_to_python_data")


def json_to_python_data(file_path: str) -> Any:
    """Функция принимает ПУТЬ к файлу JSON и преобразует его в Python список,
    либо возвращает пустой Python список.
     Пример пути к файлу: '../data/operations.json'"""
    json_to_python_logger.info("Начало работы программы")

    python_data = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                python_data = json.load(file)
            except json.JSONDecodeError:
                json_to_python_logger.warning("Ошибка декодирования файла. Программа возвращает пустой список.")
                print("Ошибка декодирования файла, возвращаем пустой список")
                return python_data
    except TypeError:
        json_to_python_logger.warning("Не верно указан путь. Программа возвращает пустой список.")
        print("Не верно указан путь")
        return python_data
    except FileNotFoundError:
        json_to_python_logger.warning("Файл не найден. Программа возвращает пустой список.")
        print("Файл не найден, возвращаем пустой список")
        return python_data
    json_to_python_logger.info("Программа отработала корректно. Завершение работы")
    return python_data
