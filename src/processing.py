from typing import Union


def filter_by_state(users_data_list: list[dict], state: str = "EXECUTED") -> Union[list[dict], str]:
    """
    Функция создаёт новый список из заданного списка фильтруя по заданному значению
    """
    filtered_users_list: list = list()
    if isinstance(users_data_list, list):
        for user in users_data_list:
            for key, value in user.items():
                if value == state:
                    filtered_users_list.append(user)
        return filtered_users_list
    return "Не корректно введены данные"


def sort_by_date(users_data_list: list[dict], sort_by: bool = True) -> Union[list[dict], str]:
    """
    Функция для сортировки данных пользователя по дате
    """
    if isinstance(users_data_list, list):
        if all("date" in key for key in users_data_list):
            sorted_users_list: list = sorted(users_data_list, key=lambda user_data: user_data["date"], reverse=sort_by)
            return sorted_users_list
    return "Не корректно введены данные"
