def filter_by_state(users_data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция создаёт новый список из заданного списка фильтруя по заданному значению"""
    filtered_users_data_list = list()
    for i in users_data_list:
        for key, value in i.items():
            if value == state:
                filtered_users_data_list.append(i)
    return filtered_users_data_list


def sort_by_date(user_data_list: list[dict], sort_by: bool = True) -> list[dict]:
    """Функция для сортировки данных пользователя по дате"""
    sorted_user_data_list = sorted(user_data_list, key=lambda user_data: user_data["date"], reverse=sort_by)
    return sorted_user_data_list
