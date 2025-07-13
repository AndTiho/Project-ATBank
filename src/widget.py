from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data: str) -> str:
    """Функция принимает строку с данными карты или счёта с наименованием карты или счёта и возвращает
    маску аккаунта карты банка с наименованием карты или счёта"""
    if isinstance(account_data, str):
        full_data_list: list = account_data.split()
        if len(full_data_list) > 0:
            list_alpha: list = [i for i in full_data_list if i.isalpha()]
            list_digit_check: str = full_data_list[-1]
            list_digit: str = "".join(i for i in list_digit_check if i.isdigit())
        else:
            return "Не корректно введены данные"
    else:
        return "Не корректно введены данные"
    if len(list_digit) > 0:
        if len(list_digit) == 16:
            return " ".join(list_alpha) + " " + get_mask_card_number(list_digit)
        elif len(list_digit) == 20:
            return " ".join(list_alpha) + " " + get_mask_account(list_digit)
    return "Не корректно введены данные"


def get_date(date: str) -> str:
    """Функция для отделения календарной даты от входящей строки с датой"""
    get_data: list = list(date)
    year: str = "".join(get_data[0:4])
    month: str = "".join(get_data[5:7])
    day: str = "".join(get_data[8:10])
    if year.isdigit() and month.isdigit() and day.isdigit():
        return f"{day}.{month}.{year}"
    else:
        return "Не корректно введены данные"
