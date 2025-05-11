import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, expected', [
    ('счёт 12344635867586742534', 'Счет **2534'),
    ('счет 12344635867586742534', 'Счет **2534'),
    ('Счёт 12344635867586742534', 'Счет **2534'),
    ('Счет 12344635867586742534', 'Счет **2534'),
    ('Visa 12344635867586742534', 'Длина номера банковской карты должна быть равна 16'),
    ('Счет 1234463586758674', 'Длина номера банковского счета должна быть равна 20')
])
def test_mask_account_card(value, expected):
    if (value == 'счёт 12344635867586742534' or value == 'счет 12344635867586742534'
            or value == 'Счёт 12344635867586742534'
            or value == 'Счет 12344635867586742534'):
        assert mask_account_card(value) == expected
    elif len(value[1]) == 20:
        with pytest.raises(ValueError, match=expected):
            mask_account_card(value)
    else:
        with pytest.raises(ValueError, match=expected):
            mask_account_card(value)


def test_get_date(valid_date):
    assert get_date(valid_date) == '11.03.2024'


def test_get_date_empty():
    with pytest.raises(ValueError, match='Дата не может быть пустой'):
        get_date('') == ''


def test_get_date_isdigit(not_valid_date):
    with pytest.raises(TypeError, match=r'Введите дату в корректном формате \(например, "2024-03-11" или "2024-03-11T02:26:18"\)'):
        get_date(not_valid_date)
