from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование функции filter_by_state
@pytest.mark.parametrize(
    "operations_fixture_name, state, expected",
    [
        (
            "executed_operations",
            "EXECUTED",
            [
                {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 3, "state": "EXECUTED", "date": "2019-08-04"},
            ],
        ),
        ("mixed_operations", "PENDING", [{"id": 2, "state": "PENDING"}]),
        ("mixed_operations", "EXECUTED", [{"id": 1, "state": "EXECUTED"}]),
        ("all_executed_operations", "EXECUTED", [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED"}]),
    ],
)
def test_filter_by_state(
    request: pytest.FixtureRequest, operations_fixture_name: str, state: str, expected: List[Dict[str, Any]]
) -> None:
    """Тест с использованием фикстур"""

    operations_fixture = request.getfixturevalue(operations_fixture_name)
    result = filter_by_state(operations_fixture, state)
    assert result == expected


def test_empty_list_by_state() -> None:
    """Тест с пустым списком операций"""

    assert filter_by_state([]) == "Отсутствуют данные для обработки! Проверьте правильность ввода!"


# Тестирование функции sort_by_date
@pytest.mark.parametrize(
    "sort, expected_order",
    [
        (True, [3, 1, 2]),  # Сортировка по убыванию (новые сначала)
        (False, [2, 1, 3]),  # Сортировка по возрастанию (старые сначала)
    ],
)
def test_sort_by_date(operations_with_dates: List[Dict[str, Any]], sort: bool, expected_order: List[int]) -> None:
    """Тест сортировки операций с разными датами"""

    result = sort_by_date(operations_with_dates, sort)
    assert [op["id"] for op in result] == expected_order


def test_sort_with_same_dates(operations_with_same_dates: List[Dict[str, Any]]) -> None:
    """Тест с одинаковыми датами (должны сохранить исходный порядок)"""

    result = sort_by_date(operations_with_same_dates)
    assert [op["id"] for op in result] == [1, 2, 3]


def test_empty_list_date() -> None:
    """Тест с пустым списком операций"""

    assert sort_by_date([]) == "Отсутствуют данные для обработки! Проверьте правильность ввода!"
