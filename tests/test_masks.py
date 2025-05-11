import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('4276070016273489', '4276 07** **** 3489'),
    ('abcddsefsdffdsf', 'На номере карты символы отсутствуют, введите числа'),
    ('42760700162734891234', 'Длина номера банковской карты должна быть равна 16')
])
def test_get_mask_card_number(value, expected):
    if value == '4276070016273489':
        assert get_mask_card_number(value) == expected
    elif value.isdigit() is True:
        with pytest.raises(ValueError, match=expected):
            get_mask_card_number(value)
    else:
        with pytest.raises(TypeError, match=expected):
            get_mask_card_number(value)


@pytest.mark.parametrize('value, expected', [
    ('42761234932475687234', '**7234'),
    ('abcddsefsdffdsf', 'На номере счета символы отсутствуют, введите числа'),
    ('427607001627348912346516116', 'Длина номера банковского счета должна быть равна 20')
])
def test_get_mask_account(value, expected):
    if value == '42761234932475687234':
        assert get_mask_account(value) == expected
    elif value.isdigit() is True:
        with pytest.raises(ValueError, match=expected):
            get_mask_account(value)
    else:
        with pytest.raises(TypeError, match=expected):
            get_mask_account(value)
