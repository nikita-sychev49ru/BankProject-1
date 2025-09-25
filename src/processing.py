from datetime import datetime
from typing import Dict, List, Union
from src.widget import get_date


def filter_by_state(operations: List[dict], state: str = "EXECUTED") -> Union[List, str]:
    """Функция фильтрации по ключу"""

    list_of_operation = [operation for operation in operations if operation.get("state", "UNKNOWN") == state]
    unknown_status_list = [operation for operation in operations if operation.get("state", "UNKNOWN") == "UNKNOWN"]
    if len(operations) == 0:
        return "Отсутствуют данные для обработки! Проверьте правильность ввода!"
    elif len(unknown_status_list) != 0:
        return "Статус одной или нескольких операций не указан!"
    elif len(list_of_operation) == 0:
        return "Операции с данным статусом отсутствуют"
    else:
        return list_of_operation


def sort_by_date(operations: list[dict], sort: bool = True) -> Union[List, str]:
    """Функция сортировки операций по дате"""

    unknown_date_list: list = [operation for operation in operations if operation.get("date", "UNKNOWN") == "UNKNOWN"]
    filter_by_wrong_date_list: list = [
        operation
        for operation in operations
        if get_date(operation.get("date", "UNKNOWN")) == "Проверьте правильность ввода!"
    ]
    if len(operations) == 0:
        return "Отсутствуют данные для обработки! Проверьте правильность ввода!"
    elif len(unknown_date_list) != 0:
        return "Дата и время одной или нескольких операций не указаны!"
    elif len(filter_by_wrong_date_list) != 0:
        return "Дата и время одной или нескольких операций имеют неверный формат!"
    else:
        sort_by_date_list = sorted(operations, key=lambda operation: operation["date"], reverse=sort)
        return sort_by_date_list
