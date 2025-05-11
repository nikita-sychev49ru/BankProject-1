def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""

    if number_card.isdigit() is True:
        if len(number_card) == 16:
            return number_card[0:4] + " " + number_card[4:6] + "**" + " " + "****" + " " + number_card[-4:]
        raise ValueError('Длина номера банковской карты должна быть равна 16')
    raise TypeError('На номере карты символы отсутствуют, введите числа')


def get_mask_account(number_acc: str) -> str:
    """Функция маскировки номера банковского счета"""

    if number_acc.isdigit() is True:
        if len(number_acc) == 20:
            return "**" + number_acc[-4:]
        raise ValueError('Длина номера банковского счета должна быть равна 20')
    raise TypeError('На номере счета символы отсутствуют, введите числа')
