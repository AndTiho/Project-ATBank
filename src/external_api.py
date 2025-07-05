import os
from typing import Dict

import requests
from dotenv import load_dotenv
from requests import HTTPError

load_dotenv()
api_key = os.getenv("API_KEY")

url = "http://api.apilayer,com/exchangerates_data/convert"
headers = {"apikey": api_key}


def operation_amount(transaction_data: dict) -> float:
    """
    Функция для вывода суммы транзакции с конвертацией USD, EUR в RUB с использованием
     AIP сайта конвертации валют.
    """
    if not isinstance(transaction_data, dict):
        raise TypeError("Не корректные данные")
    url = "http://api.apilayer.com/exchangerates_data/convert"  # Тут адрес на конвертер
    headers = {"apikey": api_key}  # Тут храним наш ключ

    try:
        # Определяем валюту транзакции
        currency_code = transaction_data["operationAmount"]["currency"]["code"]
        amount = transaction_data["operationAmount"]["amount"]

        # Работаем с USD
        if currency_code == "USD":
            payload: Dict[str, str] = {"amount": amount, "from": "USD", "to": "RUB"}
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()
            result = response.json()
            amount_sum = result.get("result")

        # Работаем с EUR
        elif currency_code == "EUR":
            payload = {"amount": amount, "from": "EUR", "to": "RUB"}
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()
            result = response.json()
            amount_sum = result.get("result")

        # Работаем с RUB
        elif currency_code == "RUB":
            amount_sum = amount

        else:
            raise ValueError(f"Неподдерживаемая валюта: {currency_code}")

    except requests.exceptions.ConnectionError:
        raise ConnectionError("Ошибка подключения. Проверьте интернет-соединение")
    except requests.exceptions.HTTPError:
        raise HTTPError("HTTP ошибка. Проверьте URL или API ключ")
    except requests.exceptions.Timeout:
        raise TimeoutError("Превышено время ожидания. Проверьте интернет-соединение")
    except ValueError as e:
        raise ValueError(f"Ошибка: {e}")

    return float(amount_sum)
