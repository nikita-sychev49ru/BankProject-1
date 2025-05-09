def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по ключу"""

    list_operations = []
    for i in operations:
        if state in i["state"]:
            list_operations.append(i)
    return list_operations


def sort_by_date(operations: list[dict], sort: bool = True) -> list[dict]:
    """Функция сортировки операций по дате"""

    sorted_operations = sorted(operations, key=lambda item: item["date"], reverse=sort)
    return sorted_operations
