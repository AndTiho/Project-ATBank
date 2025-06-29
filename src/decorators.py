from datetime import datetime
from typing import Callable, ParamSpec, TypeVar, Union

# Это для более корректного обозначения типов
P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Union[str, None]) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для логирования выполнения функций.

    Параметры:
    filename (str): путь к файлу для записи логов.
    При его отсутствии, результаты выводятся в консоль.
    """

    def logging(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                end_time = datetime.now()
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"\nStart at {start_time}\n"
                            f"{func.__name__} error : {e}. Inputs: {args}, {kwargs}\n"
                            f"Ended at {end_time}\n"
                        )
                else:
                    print(
                        f"\nStart at {start_time}\n"
                        f"{func.__name__} error : {e}. Inputs: {args}, {kwargs}\n"
                        f"Ended at {end_time}\n"
                    )
                raise
            else:
                end_time = datetime.now()
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"\nStart at {start_time}\n"
                            f"{func.__name__} ok. Result = {result}\n"
                            f"Ended at {end_time}\n"
                        )
                else:
                    print(
                        f"\nStart at {start_time}\n"
                        f"{func.__name__} ok. Result = {result}\n"
                        f"Ended at {end_time}\n"
                    )
                return result

        return wrapper

    return logging
