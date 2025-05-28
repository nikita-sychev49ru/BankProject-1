import os

from src.utils import get_transactions


def test_get_transactions1() -> None:
    """Тест для функции чтения транзакций
    из json-файла - успешная отработка"""

    utils_dir = os.path.dirname(__file__)
    data_path = os.path.join(utils_dir, "..", "data", "operations.json")
    assert get_transactions(data_path)[1] == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_get_transactions2() -> None:
    """Тест для функции чтения транзакций
    из json-файла - ошибка, файл не найден"""

    data_path = "..tests"
    assert get_transactions(data_path) == []


def test_get_transactions3() -> None:
    """Тест для функции чтения транзакций
    из json-файла - ошибка, файл не может быть прочитан"""

    utils_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(utils_dir, "..", "data", "data_for_example.txt")
    assert get_transactions(data_path) == []


def test_get_transactions4() -> None:
    """Тест для функции чтения транзакций
    из json-файла - данные в файле не могут быть преобразованы в словарь"""

    utils_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(utils_dir, "..", "data", "example.json")
    assert get_transactions(data_path) == []
