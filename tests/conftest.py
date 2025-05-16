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
