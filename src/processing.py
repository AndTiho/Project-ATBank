#
# def filter_by_state(users_data_list: list[dict], state: str= "EXECUTED") -> list[dict]:
#     filtered_users_data_list = list()
#     for i in users_data_list:
#         for key, value in i.items():
#             if value == state:
#                 filtered_users_data_list.append(i)
#     return filtered_users_data_list
#
# state = "CANCELED"
# users_data_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# print(filter_by_state(users_data_list, state))

# В том же модуле напишите функцию sort_by_date, которая принимает список словарей
# и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
# Функция должна возвращать новый список, отсортированный по дате (date).

from src.widget import get_date

def sort_by_date(user_data_list: list[dict], sort_by: bool = True) -> list[dict]:
    sorted_user_data_list = sorted(user_data_list, key=lambda user_data: user_data['date'], reverse = sort_by)
    return sorted_user_data_list

user_data_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(sort_by_date(user_data_list))