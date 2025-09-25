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
    return [{'id': '441945886', 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'amount': '31957.58',
             'currency_name': 'руб.', 'currency_code': 'RUB', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589', 'description': 'Перевод организации'},
            {'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'amount': '8221.37',
             'currency_name': 'USD', 'currency_code': 'USD', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560', 'description': 'Перевод организации'},
            {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'amount': '9824.07',
             'currency_name': 'USD', 'currency_code': 'USD', 'from': 'Счет 75106830613657916952',
             'to': 'Счет 11776614605963066702', 'description': 'Перевод организации'},
            {'id': '587085106', 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'amount': '48223.05',
             'currency_name': 'руб.', 'currency_code': 'RUB', 'from': None, 'to': 'Счет 41421565395219882431',
             'description': 'Открытие вклада'},
            {'id': '142264268', 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'amount': '79114.93',
             'currency_name': 'USD', 'currency_code': 'USD', 'from': 'Счет 19708645243227258542',
             'to': 'Счет 75651667383060284188', 'description': 'Перевод со счета на счет'}]


@pytest.fixture
def transactions_empty() -> list:
    return []


@pytest.fixture
def transaction_descriptions_list() -> list:
    return [
        "Перевод организации",
        "Перевод организации",
        "Перевод организации",
        "Открытие вклада",
        "Перевод со счета на счет",
    ]


@pytest.fixture
def transaction_descriptions_or_not() -> list:
    return [
        {"id": 939719570, "code": "USD"},
        {"id": 939719577, "currency_code": "USD", "description": "Перевод со счета на счет"},
    ]


# Модуль tables_reading.py
# Фикстура тестовых данных для функции get_transactions_csv
@pytest.fixture
def make_csv_transaction() -> list:
    return [{"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]


# Фикстура для функции получения суммы операции в рублях - норма, валюта - рубль
@pytest.fixture
def make_operation_for_get_amount_1() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Фикстура для функции преобразования xlsx - норма
@pytest.fixture
def make_xlsx_transaction1() -> dict:
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


# Фикстура для функции преобразования xlsx, нет значения amount
@pytest.fixture
def make_xlsx_transaction2() -> dict:
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
