import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для get_mask_card_number
def test_standard_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 7*** ***0 6361"


def test_with_symbols_get_mask_card_number():
    assert get_mask_card_number("1234*5678_9012-3456") == "1234 5*** ***2 3456"


@pytest.mark.parametrize(
    "number, expected",
    [("1234 5678 9012 345", "Не корректно введены данные"), ("1234 5678 9012 3453 2", "Не корректно введены данные")],
)
def test_long_short_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_empty_mask_card_number(empty_data):
    assert get_mask_card_number(empty_data) == "Не корректно введены данные"


def test_letters_mask_card_number(letters_string):
    assert get_mask_card_number(letters_string) == "Не корректно введены данные"


def test_not_string_mask_card_number(not_list):
    assert get_mask_card_number(not_list) == "Не корректно введены данные"


# Тесты для get_mask_account
def test_standard_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_with_symbols_mask_account():
    assert get_mask_account("7365-41084.3013.587/4305") == "**4305"


@pytest.mark.parametrize(
    "number, expected",
    [("7365410843013587430", "Не корректно введены данные"), ("736541084301358743052", "Не корректно введены данные")],
)
def test_long_short_mask_account(number, expected):
    assert get_mask_account(number) == expected


def test_empty_mask_account(empty_data):
    assert get_mask_account(empty_data) == "Не корректно введены данные"


def test_letters_mask_account(letters_string):
    assert get_mask_account(letters_string) == "Не корректно введены данные"


def test_not_string_account(not_list):
    assert get_mask_account(not_list) == "Не корректно введены данные"
