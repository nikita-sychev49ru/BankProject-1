import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("счёт 12344635867586742534", "Счет **2534"),
        ("счет 12344635867586742534", "Счет **2534"),
        ("Счёт 12344635867586742534", "Счет **2534"),
        ("Счет 12344635867586742534", "Счет **2534"),
        ("Visa 12344635867586742534", "Длина номера банковской карты должна быть равна 16"),
        ("Счет 1234463586758674", "Длина номера банковского счета должна быть равна 20"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    """Тест на опциональную маскировку продукта, проверку длины и корректности ввода вне зависимости от регистра"""

    if (
        value == "счёт 12344635867586742534"
        or value == "счет 12344635867586742534"
        or value == "Счёт 12344635867586742534"
        or value == "Счет 12344635867586742534"
    ):
        assert mask_account_card(value) == expected
    elif len(value[1]) == 20:
        with pytest.raises(ValueError, match=expected):
            mask_account_card(value)
    else:
        with pytest.raises(ValueError, match=expected):
            mask_account_card(value)


def test_mask_account_card_empty() -> None:
    """Тест с пустым списком"""

    with pytest.raises(ValueError, match="Передан пустой список"):
        mask_account_card("")


def test_get_date(valid_date: str) -> None:
    """Тест на проверку валидной даты"""

    assert get_date(valid_date) == "11.03.2024"


def test_get_date_empty() -> None:
    """Тест на проверку пустой даты"""

    with pytest.raises(ValueError, match="Дата не может быть пустой"):
        get_date("")


def test_get_date_isdigit(not_valid_date: str) -> None:
    """Тест на проверку невалидной даты"""

    with pytest.raises(
        TypeError, match=r"Введите дату в корректном формате \(например, " r'"2024-03-11" или "2024-03-11T02:26:18"\)'
    ):
        get_date(not_valid_date)
