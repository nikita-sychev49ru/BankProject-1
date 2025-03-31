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


test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
