from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("data, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 8*** ***0 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758","MasterCard 7158 3*** ***2 6758"),
    ("Счет 35383033474447895560","Счет **5560"),
    ("Visa Classic 6831982476737658","Visa Classic 6831 9*** ***3 7658"),
    ("Visa Platinum 8990922113665229","Visa Platinum 8990 9*** ***6 5229"),
    ("Visa Gold 5999414228426353","Visa Gold 5999 4*** ***2 6353"),
    ("Счет 73654108430135874305","Счет **4305")
])
def test_some_account_data(data, expected):
    assert mask_account_card(data) == expected


def test_no_data(not_list):
    assert mask_account_card(not_list) == "Не корректно введены данные"


def test_empty_data(empty_data):
    assert mask_account_card(empty_data) == "Не корректно введены данные"


@pytest.mark.parametrize("some_data, expected", [
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2018-10-14T08:21:33.419441", "14.10.2018")
]
)
def test_some_data(some_data, expected):
    assert get_date(some_data) == expected

def test_letters_string(letters_string):
    assert get_date(letters_string) == "Не корректно введены данные"