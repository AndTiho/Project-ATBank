import pytest

from src.re_utils import process_bank_operations, process_bank_search


def test_process_bank_search(transactions_data):
    assert process_bank_search(transactions_data, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_search_empty_list(empty_list):
    assert process_bank_search(empty_list, "Перевод организации") == []


def test_process_bank_search_invalid_data_type(not_list):
    with pytest.raises(TypeError) as exc_info:
        process_bank_search(not_list, "Перевод организации")
    assert "Входные данные не являются списком" in str(exc_info.value)


def test_process_bank_operations(transactions_data):
    assert process_bank_operations(transactions_data, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }


def test_process_bank_operations_empty_list(empty_list):
    assert process_bank_operations(empty_list, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 0,
        "Перевод с карты на карту": 0,
    }


def test_process_bank_operations_invalid_data_type(not_list):
    with pytest.raises(TypeError) as exc_info:
        process_bank_operations(not_list, ["Перевод организации"])
    assert "Входные данные не являются списком" in str(exc_info.value)
