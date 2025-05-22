from typing import Any

import pytest


# Модуль masks.py
# Фикстуры тестовых данных для функции get_mask_card_number
@pytest.fixture
def mask_card() -> list[tuple[str, str]]:
    return [
        ("4276070016273489", "4276 07** **** 3489"),
        ("abcddsefsdffdsf", "На номере карты символы отсутствуют, введите числа"),
        ("42760700162734891234", "Длина номера банковской карты должна быть равна 16"),
    ]


# Фикстуры тестовых данных для функции get_mask_account
@pytest.fixture
def mask_account() -> list[tuple[str, str]]:
    return [
        ("42761234932475687234", "**7234"),
        ("abcddsefsdffdsf", "На номере счета символы отсутствуют, введите числа"),
        ("427607001627348912346516116", "Длина номера банковского счета должна быть равна 20"),
    ]


# Модуль widget.py
# Фикстуры тестовых данных для функции mask_account_card
@pytest.fixture
def mask_product() -> list[tuple[str, str]]:
    return [
        ("счёт 12344635867586742534", "Счет **2534"),
        ("счет 12344635867586742534", "Счет **2534"),
        ("Счёт 12344635867586742534", "Счет **2534"),
        ("Счет 12344635867586742534", "Счет **2534"),
        ("Visa 12344635867586742534", "Длина номера банковской карты должна быть равна 16"),
        ("Счет 1234463586758674", "Длина номера банковского счета должна быть равна 20"),
    ]


# Фикстуры тестовых данных для функции get_date
@pytest.fixture
def not_valid_date() -> str:
    return "11 марта 2024"


@pytest.fixture
def valid_date() -> str:
    return "2024-03-11T02:26:18.671407"


# Модуль processing.py
# Фикстуры тестовых данных для функции filter_by_state
@pytest.fixture
def executed_operations() -> list[dict[str, object]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED", "date": "2019-08-04"},
    ]


@pytest.fixture
def mixed_operations() -> list[dict[str, object]]:
    return [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "CANCELED"}]


@pytest.fixture
def all_executed_operations() -> list[dict[str, object]]:
    return [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED"}]


# Фикстуры тестовых данных для функции sort_by_date
@pytest.fixture
def operations_with_dates() -> list[dict[str, object]]:
    return [
        {"id": 1, "date": "2023-01-15T12:00:00"},
        {"id": 2, "date": "2023-01-10T08:30:00"},
        {"id": 3, "date": "2023-01-20T18:45:00"},
    ]


@pytest.fixture
def operations_with_same_dates() -> list[dict[str, object]]:
    return [
        {"id": 1, "date": "2023-01-10T00:00:00"},
        {"id": 2, "date": "2023-01-10T00:00:00"},
        {"id": 3, "date": "2023-01-10T00:00:00"},
    ]


# Модуль generators.py
# Фикстуры тестовых данных для функции filter_by_currency
@pytest.fixture
def transactions() -> Any:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_empty() -> list:
    return []


@pytest.fixture
def transaction_descriptions_list() -> list:
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def transaction_descriptions_or_not() -> list:
    return [
        {"id": 939719570, "code": "USD"},
        {"id": 939719577, "currency_code": "USD", "description": "Перевод со счета на счет"},
    ]
