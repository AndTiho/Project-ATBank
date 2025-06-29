import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "http://api.apilayer,com/exchangerates_data/convert"
headers = {"apikey": api_key}


def operation_amount(transaction_data: dict) -> float:
    """
    Функция для подсчёта общей суммы всех транзакций с конвертацией в RUB
    с использованием AIP сайта конвертации валют
    """
    amount_sum: float = 0.0  # Тут у нас переменная для конечного итога выводимого на баланс юзера
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
            amount_sum = float(result.get("result"))

        # Работаем с EUR
        elif currency_code == "EUR":
            payload = {"amount": amount, "from": "EUR", "to": "RUB"}
            response = requests.get(url, headers=headers, params=payload)
            response.raise_for_status()
            result = response.json()
            amount_sum = float(result.get("result"))

        # Работаем с RUB
        elif currency_code == "RUB":
            amount_sum = amount

        else:
            raise ValueError(f"Неподдерживаемая валюта: {currency_code}")

    except requests.exceptions.ConnectionError:
        print("Ошибка подключения. Проверьте интернет-соединение")
    except requests.exceptions.HTTPError:
        print("HTTP ошибка. Проверьте URL или API ключ")
    except requests.exceptions.Timeout:
        print("Превышено время ожидания. Проверьте интернет-соединение")
    except ValueError as e:
        print(f"Ошибка: {e}")

    return amount_sum
