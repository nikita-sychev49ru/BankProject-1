from datetime import datetime


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по ключу"""

    if not operations:
        raise ValueError("Передан пустой список операций")
    list_operations = []
    for i in operations:
        if state in i["state"]:
            list_operations.append(i)
    return list_operations


def sort_by_date(operations: list[dict], sort: bool = True) -> list[dict]:
    """Функция сортировки операций по дате"""

    for op in operations:
        if "date" not in op:
            raise KeyError('Отсутствует ключ "date"')
        try:
            # Проверяем формат даты (ожидаем формат YYYY-MM-DD)
            datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            raise ValueError("Некорректный формат даты")

        # Сортируем операции по дате
    sorted_operations = sorted(operations, key=lambda item: item["date"], reverse=sort)
    return sorted_operations
