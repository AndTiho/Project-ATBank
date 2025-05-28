def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    mask_card_number: list = list(card_number)

    for i in range(5, 11):
        mask_card_number[i] = "*"

    return " ".join("".join(mask_card_number[i : i + 4]) for i in range(0, len(mask_card_number), 4))


def get_mask_account(account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    return "".join(["**", account[-4:]])
