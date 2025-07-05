from typing import Any, Generator


def filter_by_currency(transactions: list[dict], value: str) -> Generator[Any, Any, None]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    gen_filter_by_currency = filter(
        lambda data: data.get("operationAmount", {}).get("currency", {}).get("code") == value, transactions
    )
    for feltered_value in gen_filter_by_currency:
        yield feltered_value


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction["description"]
        else:
            yield "В данных нет записи о виде транзакции"


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """Генератор, который выдает номера банковских карт в формате: XXXX XXXX XXXX XXXX, где X— цифра номера карты.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    if not isinstance(start, int) and not isinstance(end, int):
        yield "Некорректные параметры диапазона"
    if start < 0 or end < 0 or start > end:
        yield "Некорректные параметры диапазона"
    for x in range(start, end + 1):
        x_str = str(x)
        if len(x_str) < 16:
            x_str = (16 - len(x_str)) * "0" + x_str
            yield " ".join("".join(x_str[i : i + 4]) for i in range(0, len(x_str), 4))
        else:
            yield "Превышена max длинна в параметрах"
