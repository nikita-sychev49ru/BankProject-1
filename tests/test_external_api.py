from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import get_amount_transaction


@patch("requests.get")
def test_get_amount_transaction1(mock_get_amount: Any) ->None:
    """Тест для функции конвертации суммы в рублях - успешная отработка"""

    mock_get_amount.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1748135764, "rate": 79.342042},
        "date": "2025-05-25",
        "result": 652300.283838,
    }
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    assert get_amount_transaction(transaction) == "Сумма транзакции в рублях: 652300.283838"
    mock_get_amount.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37&"
        "apikey=ET8qjUQNBxdJKOFnDW8g7f1hSk1QYcFu"
    )


def test_get_amount_transaction2(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции конвертации суммы в рублях - ошибка, некорректный тип данных"""

    get_amount_transaction(123)
    captured = capsys.readouterr()
    output = captured.out
    assert "Некорректный тип данных" in output


def test_get_amount_transaction3(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции конвертации суммы в рублях - ошибка запроса 429"""

    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    # Mock-ответ с ошибкой 429
    mock_response = Mock()
    mock_response.status_code = 429
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("429 Too Many Requests")

    # Мокируем requests.get
    with patch("requests.get", return_value=mock_response):
        get_amount_transaction(transaction)
        captured = capsys.readouterr()
        output = captured.out
        assert "Ошибка запроса 429 Too Many Requests" in output
