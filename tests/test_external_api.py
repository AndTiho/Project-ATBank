from unittest.mock import patch
import pytest
import requests
from requests.exceptions import HTTPError

from src.external_api import operation_amount


def test_current_work_rub(for_converter_rub):
    assert (operation_amount(for_converter_rub)) == 1.07


def test_current_work_usd(one_trans_data):
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json.return_value = {"result": 9000}
        result = operation_amount(one_trans_data)
    assert result == 9000


def test_current_work_eur():
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.json.return_value = {"result": 10000}
        result = operation_amount({"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}})
    assert result == 10000


def test_type_error(letters_string):
    with pytest.raises(TypeError):
        operation_amount(letters_string)


# Тест для проверки неподдерживаемой валюты
def test_unsupported_currency(for_converter_jpy):
    with pytest.raises(ValueError) as exc_info:
        operation_amount(for_converter_jpy)
    assert str(exc_info.value) == "Ошибка: Неподдерживаемая валюта: JPY"


# Тест для проверки ошибки подключения
def test_connection_error(one_trans_data):
    with patch("requests.get") as mocked_get:
        mocked_get.side_effect = requests.exceptions.ConnectionError()
        with pytest.raises(ConnectionError) as exc_info:
            operation_amount(one_trans_data)
        assert str(exc_info.value) == "Ошибка подключения. Проверьте интернет-соединение"


# Тест для проверки HTTP ошибки
def test_http_error(one_trans_data):
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        with pytest.raises(HTTPError) as exc_info:
            operation_amount(one_trans_data)
        assert str(exc_info.value) == "HTTP ошибка. Проверьте URL или API ключ"


# Тест для проверки ошибки таймаута
def test_timeout_error(one_trans_data):
    with patch("requests.get") as mocked_get:
        mocked_get.side_effect = requests.exceptions.Timeout()
        with pytest.raises(TimeoutError) as exc_info:
            operation_amount(one_trans_data)
        assert str(exc_info.value) == "Превышено время ожидания. Проверьте интернет-соединение"
