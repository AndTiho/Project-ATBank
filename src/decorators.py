from datetime import datetime


def log(filename):
    """
        Декоратор для логирования выполнения функций.

        Параметры:
        filename (str): путь к файлу для записи логов.
        При его отсутствии, результаты выводятся в консоль.
    """
    def logging(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args,**kwargs)
            except Exception as e:
                end_time = datetime.now()
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"\nStart at {start_time}\n"
                                   f"{func.__name__} error : {e}. Inputs: {args}, {kwargs}\n"
                                   f"Ended at {end_time}\n")
                else:
                    print(f"\nStart at {start_time}\n"
                          f"{func.__name__} error : {e}. Inputs: {args}, {kwargs}\n"
                          f"Ended at {end_time}\n")
            else:
                end_time = datetime.now()
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"\nStart at {start_time}\n"
                                   f"{func.__name__} ok. Result = {result}\n"
                                   f"Ended at {end_time}\n")
                else:
                    print(f"\nStart at {start_time}\n"
                          f"{func.__name__} ok. Result = {result}\n"
                          f"Ended at {end_time}\n")
                return result
        return wrapper
    return logging

@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(1, 0)


# @log(filename="")
# def my_function(x, y):
#     return x + y
#
# my_function(1, 2)
