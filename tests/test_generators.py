from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тесты для filter_by_currency
def test_filter_by_currency_usd(transactions_data):
    generator = filter_by_currency(transactions_data, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_rub(transactions_data):
    generator = filter_by_currency(transactions_data, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_none(transactions_data):
    generator = filter_by_currency(transactions_data, "EURO")
    assert next(generator, None) is None


def test_filter_by_currency(empty_list):
    assert list(filter_by_currency(empty_list, "RUB")) == []


# Тесты для transaction_descriptions


def test_transaction_descriptions_common(transactions_data):
    generator = transaction_descriptions(transactions_data)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_empty(empty_list):
    assert next(transaction_descriptions(empty_list)) == "В данных нет записи о виде транзакции"


def test_transaction_descriptions_no_descr(transactions_data_no_descr):
    generator = transaction_descriptions(transactions_data_no_descr)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "В данных нет записи о виде транзакции"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


# Тесты для card_number_generator


def test_card_number_generator_common():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_card_number_generator_more_then_16():
    generator = card_number_generator(59865943265948531, 59865943265948981)
    assert next(generator) == "Превышена max длинна в параметрах"


def test_card_number_generator_negative_numbers():
    generator = card_number_generator(-3545, 654254)
    assert next(generator) == "Некорректные параметры диапазона"


def test_card_number_generator_zero():
    generator = card_number_generator(0, 0)
    assert next(generator) == "0000 0000 0000 0000"


def test_card_number_generator_float():
    generator = card_number_generator(3.23, 4.412)
    assert next(generator) == "Некорректные параметры диапазона"
