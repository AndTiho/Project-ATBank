import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

mask_account_logger = logging.getLogger("app.masks_get_mask_card_number")
mask_card_logger = logging.getLogger("app.masks_get_mask_account")


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    mask_card_logger.info("Запуск модуля")
    mask_card_logger.info(f"Получение данных {card_number}")

    if not isinstance(card_number, str):
        mask_card_logger.error(f"{card_number}: не является строкой. Завершение работы")
        return "Не корректно введены данные"
    mask_card_number: list = list("".join(num for num in card_number if num.isdigit()))
    if len(mask_card_number) != 16:
        mask_card_logger.error(f"{card_number}: содержит неверное число символов (16). Завершение работы")
        return "Не корректно введены данные"
    for i in range(5, 11):
        mask_card_number[i] = "*"

    mask_card_logger.info("Функция отработала корректно. Завершение работы")
    return " ".join("".join(mask_card_number[i : i + 4]) for i in range(0, len(mask_card_number), 4))


def get_mask_account(account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    mask_account_logger.info("Запуск работы модуля.")

    if not isinstance(account, str):
        mask_account_logger.error(f"{account}: введённые данные не являются строкой. Завершение работы..")
        return "Не корректно введены данные"
    mask_account: str = "".join(num for num in account if num.isdigit())
    if len(mask_account) != 20:
        mask_account_logger.error(
            f"{len(mask_account)}: Длина номера не соответствует требованиям в 20 символов. Завершение работы.."
        )
        return "Не корректно введены данные"
    mask_account_logger.info("Программа отработала корректно. Завершение работы")
    return "".join(["**", mask_account[-4:]])
