def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""

    return number_card[0:4] + " " + number_card[4:6] + "**" + " " + "****" + " " + number_card[-4:]


def get_mask_account\
                (number_acc: str) -> str:
    """Функция маскировки номера банковского счета"""

    return "**" + number_acc[-4:]
