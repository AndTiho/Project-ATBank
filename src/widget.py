from typing import Any

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> Any:
    full_data_list: list = account_data.split(" ")
    list_alpha: list = [i for i in full_data_list if i.isalpha()]
    list_digit: list = [i for i in full_data_list if i.isdigit()]

    if len(list_digit[0]) == 16:
        return " ".join(list_alpha) + " " + get_mask_card_number("".join(list_digit))
    elif len(list_digit[0]) == 20:
        return " ".join(list_alpha) + " " + get_mask_account("".join(list_digit))
    else:
        return None


def get_date(date: str) -> str:
    get_data: list = list(date)
    year: str = "".join(get_data[0:4])
    month: str = "".join(get_data[5:7])
    day: str = "".join(get_data[8:10])
    return day + "." + month + "." + year

