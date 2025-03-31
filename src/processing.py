def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрации по ключу"""

    list_operations = []
    for i in operations:
        if state in i['state']:
            list_operations.append(i)
    return list_operations

