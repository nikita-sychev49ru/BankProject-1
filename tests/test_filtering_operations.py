from unittest.mock import patch

from src.filtering_operations import (
    get_count_category,
    get_transactions_optional_format,
    normalize_transaction,
    search_transactions,
)


def test_get_transactions_optional_format1() -> None:
    """Тест для функции чтения списка операций - норма, чтение JSON"""

    with (
        patch("builtins.input", return_value="1"),
        patch("src.filtering_operations.get_transactions") as mock_get_ops,
        patch("src.filtering_operations.normalize_transaction") as mock_norm,
    ):
        mock_get_ops.return_value = [{"id": 1}, {"id": 2}]
        mock_norm.side_effect = lambda x: x
        result = get_transactions_optional_format()
        assert result[1] == {"id": 2}
    mock_get_ops.assert_called_once()
    mock_norm.assert_called()


def test_get_transactions_optional_format2() -> None:
    """Тест для функции чтения списка операций - норма, чтение CSV"""

    with (
        patch("builtins.input", return_value="2"),
        patch("src.filtering_operations.get_transactions_csv") as mock_get_ops,
    ):
        mock_get_ops.return_value = [{"id": 1}, {"id": 2}]
        result = get_transactions_optional_format()
        assert result[1] == {"id": 2}
    mock_get_ops.assert_called_once()


def test_get_transactions_optional_format3() -> None:
    """Тест для функции чтения списка операций - норма, чтение XLSX"""

    with (
        patch("builtins.input", return_value="3"),
        patch("src.filtering_operations.get_transactions_xlsx") as mock_get_ops,
        patch("src.filtering_operations.normalize_transaction") as mock_norm,
    ):
        mock_get_ops.return_value = [{"id": 1}, {"id": 2}]
        mock_norm.side_effect = lambda x: x
        result = get_transactions_optional_format()
        assert result[1] == {"id": 2}
    mock_get_ops.assert_called_once()
    mock_norm.assert_called()


def test_get_transactions_optional_format4() -> None:
    """Тест для функции чтения списка операций - ошибка, введен неверный код"""

    with patch("builtins.input", return_value="0"):
        result = get_transactions_optional_format()
        assert result == "Ошибка ввода! Данные не найдены!"


def test_normalize_transaction1(make_operation_for_get_amount_1: dict) -> None:
    """Тест для функции приведения операций к единому формату -
    норма, работа над форматом, возвращаемым JSON"""

    result = normalize_transaction(make_operation_for_get_amount_1)
    assert result == {
        "amount": "31957.58",
        "currency_code": "RUB",
        "currency_name": "руб.",
        "date": "2019-08-26T10:50:58.294041",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "id": "441945886",
        "state": "EXECUTED",
        "to": "Счет 64686473678894779589",
    }


def test_normalize_transaction2(make_xlsx_transaction1: dict) -> None:
    """Тест для функции приведения операций к единому формату -
    норма, работа над форматом, возвращаемым XLSX"""

    result = normalize_transaction(make_xlsx_transaction1)
    assert result.get("id") == "650703.0"


def test_normalize_transaction3(make_xlsx_transaction2: dict) -> None:
    """Тест для функции приведения операций к единому формату -
    работа над форматом, возвращаемым XLSX, нет ключа amount"""

    result = normalize_transaction(make_xlsx_transaction2)
    assert result.get("amount") == "0"


def test_search_transactions1() -> None:
    """Тест для функции поиска операций по ключевому слову - норма"""

    transactions = [{"id": 1, "state": "ok"}, {"id": 2, "state": "failed"}, {"id": 3, "state": "ok"}]
    result = search_transactions(transactions, target="ok")
    assert result == [{"id": 1, "state": "ok"}, {"id": 3, "state": "ok"}]


def test_search_transactions2() -> None:
    """Тест для функции поиска операций по ключевому слову -
    ошибка, неверный формат ключевого слова"""

    transactions = [{"id": 1, "state": "ok"}, {"id": 2, "state": "failed"}, {"id": 3, "state": "ok"}]
    result = search_transactions(transactions, target=1)
    assert result == []


def test_search_transactions3() -> None:
    """Тест для функции поиска операций по ключевому слову -
    операции соответствующие критериям поиска отсутствуют"""

    transactions = [{"id": 1, "state": "ok"}, {"id": 2, "state": "failed"}, {"id": 3, "state": "ok"}]
    result = search_transactions(transactions, target="well")
    assert result == []


def test_get_count_category1() -> None:
    """Тест для функции подсчета количества операций по категориям -
    норма"""

    transactions = [{"id": 1, "description": "ok"}, {"id": 2, "description": "failed"}, {"id": 3, "description": "ok"}]
    result = get_count_category(transactions, ["ok", "failed"])
    assert result == {"ok": 2, "failed": 1}


def test_get_count_category2() -> None:
    """Тест для функции подсчета количества операций по категориям -
    не найдено соответствующих критериям отбора операций"""

    transactions = [{"id": 1, "description": "ok"}, {"id": 2, "description": "failed"}, {"id": 3, "description": "ok"}]
    result = get_count_category(transactions, ["start", "stop"])
    assert result == {"start": 0, "stop": 0}


def test_get_count_category3() -> None:
    """Тест для функции подсчета количества операций по категориям -
    нет нужного ключа, неверный формат данных значения по ключу"""

    transactions = [{"id": 1, "descript": "ok"}, {"id": 2, "description": "failed"}, {"id": 3, "description": None}]
    result = get_count_category(transactions, ["ok", "failed"])
    assert result == {"ok": 0, "failed": 1}
