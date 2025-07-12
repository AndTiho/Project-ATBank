from src.csv_excel_utils import csv_to_python_data, excel_to_python_data
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.re_utils import process_bank_search
from src.utils import json_to_python_data
from src.widget import get_date, mask_account_card

global after_sort_data


def main():  # type: ignore[no-untyped-def]
    global after_sort_data
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_answer = int(input())
    while user_answer not in [1, 2, 3]:
        user_answer = input("Выберите из доступных команд 1, 2 или 3")

    if user_answer == 1:
        print("Для обработки выбран JSON-файл")
        json_file = json_to_python_data("./data/operations.json")
        data_state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        while data_state not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {data_state} недоступен")
            data_state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            ).upper()
        filtered_data = filter_by_state(json_file, data_state)
        print(f"Операции отфильтрованы по статусу {data_state}")

        print("Отсортировать операции по дате? Да/Нет")
        sort_by_date_question = input().lower()
        if sort_by_date_question == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            sort_by_question = input().lower()
            if sort_by_question == "по убыванию":
                after_sort_data = sort_by_date(filtered_data, sort_by=False)
            else:
                after_sort_data = sort_by_date(filtered_data, sort_by=True)
        else:
            after_sort_data = filtered_data

        print("Выводить только рублевые транзакции? Да/Нет")
        filter_by_currency_question = input().lower()
        if filter_by_currency_question == "да":
            after_filter_by_currency = list(filter_by_currency(after_sort_data, "RUB"))
        else:
            after_filter_by_currency = after_sort_data

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter_by_word = input().lower()
        if filter_by_word == "да":
            word = input("Введите слово для фильтра\n")
            result = process_bank_search(after_filter_by_currency, word)
        else:
            result = after_filter_by_currency

        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке {len(result)}\n")
        if len(result) != 0:
            for r in result:
                amount = r.get("operationAmount").get("amount")
                code = r.get("operationAmount").get("currency").get("name")
                if r["description"] == "Открытие вклада":
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('to'))}\n"
                        f"Сумма: {amount} {code}\n"
                    )
                else:
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('from'))} -> {mask_account_card(r.get('to'))}\n"
                        f"Сумма: {amount} {code}\n"
                    )
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    if user_answer == 2:
        print("Для обработки выбран CSV-файл")
        csv_list = csv_to_python_data("./data/transactions.csv")
        data_state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        while data_state not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {data_state} недоступен")
            data_state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            ).upper()
        filtered_data = filter_by_state(csv_list, data_state)
        print(f"Операции отфильтрованы по статусу {data_state}")

        print("Отсортировать операции по дате? Да/Нет")
        sort_by_date_question = input().lower()
        if sort_by_date_question == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            sort_by_question = input().lower()
            if sort_by_question == "по убыванию":
                after_sort_data = sort_by_date(filtered_data, sort_by=False)
            else:
                after_sort_data = sort_by_date(filtered_data, sort_by=True)
        else:
            after_sort_data = filtered_data
        print("Выводить только рублевые транзакции? Да/Нет")
        filter_by_currency_question = input().lower()
        if filter_by_currency_question == "да":
            after_filter_by_currency = list(filter(lambda data: data.get("currency_code") == "RUB", after_sort_data))
        else:
            after_filter_by_currency = after_sort_data

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter_by_word = input().lower()
        if filter_by_word == "да":
            word = input("Введите слово для фильтра\n")
            result = process_bank_search(after_filter_by_currency, word)
        else:
            result = after_filter_by_currency

        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке {len(result)}\n")
        if len(result) != 0:
            for r in result:
                if r["description"] == "Открытие вклада":
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('to'))}\n"
                        f"Сумма: {r.get('amount')} {r.get('currency_name')}\n"
                    )
                else:
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('from'))} -> {mask_account_card(r.get('to'))}\n"
                        f"Сумма: {r.get('amount')} {r.get('currency_name')}\n"
                    )
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    if user_answer == 3:
        print("Для обработки выбран XLSX-файл")
        excel_data = excel_to_python_data("./data/transactions_excel.xlsx")
        data_state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        while data_state not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {data_state} недоступен")
            data_state = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            ).upper()
        filtered_data = filter_by_state(excel_data, data_state)
        print(f"Операции отфильтрованы по статусу {data_state}")

        print("Отсортировать операции по дате? Да/Нет")
        sort_by_date_question = input().lower()
        if sort_by_date_question == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            sort_by_question = input().lower()
            if sort_by_question == "по убыванию":
                after_sort_data = sort_by_date(filtered_data, sort_by=False)
            else:
                after_sort_data = sort_by_date(filtered_data, sort_by=True)
        else:
            after_sort_data = filtered_data
        print("Выводить только рублевые транзакции? Да/Нет")
        filter_by_currency_question = input().lower()
        if filter_by_currency_question == "да":
            after_filter_by_currency = list(filter(lambda data: data.get("currency_code") == "RUB", after_sort_data))
        else:
            after_filter_by_currency = after_sort_data

        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter_by_word = input().lower()
        if filter_by_word == "да":
            word = input("Введите слово для фильтра\n")
            result = process_bank_search(after_filter_by_currency, word)
        else:
            result = after_filter_by_currency

        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке {len(result)}\n")
        if len(result) != 0:
            for r in result:
                if r["description"] == "Открытие вклада":
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('to'))}\n"
                        f"Сумма: {r.get('amount')} {r.get('currency_name')}\n"
                    )
                else:
                    print(
                        f"\n{get_date(r.get('date'))} {r['description']}\n"
                        f"{mask_account_card(r.get('from'))} -> {mask_account_card(r.get('to'))}\n"
                        f"Сумма: {r.get('amount')} {r.get('currency_name')}\n"
                    )
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
