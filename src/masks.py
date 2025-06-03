def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    if not isinstance(card_number, str):
        return "Не корректно введены данные"
    mask_card_number: list = list(''.join(num for num in card_number if num.isdigit()))
    if len(mask_card_number) != 16:
        return "Не корректно введены данные"
    for i in range(5, 11):
        mask_card_number[i] = "*"
    return " ".join("".join(mask_card_number[i : i + 4]) for i in range(0, len(mask_card_number), 4))


def get_mask_account(account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    if not isinstance(account, str):
        return "Не корректно введены данные"
    mask_account: str = ''.join(num for num in account if num.isdigit())
    if len(mask_account) != 20:
        return "Не корректно введены данные"
    return "".join(["**", mask_account[-4:]])
