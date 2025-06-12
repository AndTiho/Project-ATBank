from typing import Any, Generator


def filter_by_currency(transactions: list[dict], value: str) -> Generator[Any, Any, None]:
    gen_filter_by_currency = filter(lambda data: data["operationAmount"]["currency"]["code"] == value, transactions)
    for feltered_value in gen_filter_by_currency:
        yield feltered_value


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    for description in transactions:
        yield description["description"]


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    if start < 0 or end < 0 or start > end:
        raise ValueError("Некорректные параметры диапазона")
    for x in range(start, end + 1):
        x_str = str(x)
        if len(x_str) < 16:
            x_str = (16 - len(x_str)) * "0" + x_str
        yield " ".join("".join(x_str[i : i + 4]) for i in range(0, len(x_str), 4))

