import os
import datetime
from functools import wraps
from typing import Any, Optional, Callable


def log(filename: Optional[str] = None) -> Any:
    """Декоратор, который автоматически логирует начало и выполнения
        функции, а так же её результаты или возникшие ошибки"""

    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                success_msg = (f"Начало выполнения функции: {start_time}\n"
                               f"Функция {func.__name__} выполнена успешно.\n"
                               f"Конец выполнения функции: {end_time}\n"
                               f"Входные параметры: {args, kwargs}\n"
                               f"Результат: {result}")
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{success_msg}\n"
                                   f"----------------------------\n")
                else:
                    print(success_msg)
                return result

            except Exception as e:
                error_time = datetime.datetime.now()
                error_msg = (f"Начало выполнения функции: {start_time}\n"
                             f"Функция {func.__name__} выполнена безуспешно, возникла ошибка!\n"
                             f"Конец выполнения функции: {error_time}\n"
                             f"Тип ошибки: {type(e)}, {e}\n"
                             f"Входные параметры: {args, kwargs}")
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{error_msg}\n"
                                   f"----------------------------\n")
                else:
                    print(f"{error_msg}")

        return wrapper

    return inner
