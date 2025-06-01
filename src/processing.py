def filter_by_state(users_data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция создаёт новый список из заданного списка фильтруя по заданному значению
    """
    filtered_users_list: list = list()

    for user in users_data_list:
        for key, value in user.items():
            if value == state:
                filtered_users_list.append(user)

    return filtered_users_list


def sort_by_date(users_data_list: list[dict], sort_by: bool = True) -> list[dict]:
    """
    Функция для сортировки данных пользователя по дате
    """
    sorted_users_list: list = sorted(users_data_list, key=lambda user_data: user_data["date"], reverse=sort_by)
    return sorted_users_list
