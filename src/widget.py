from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты и счета"""

    if not account_card:
        raise ValueError("Передан пустой список")
    account_card_split = account_card.split()
    # Маскировка счета
    if any(word.lower() in {"счет", "счёт"} for word in account_card_split):
        if len(account_card_split[1]) == 20:
            return f"Счет {get_mask_account(account_card_split[1])}"
        raise ValueError("Длина номера банковского счета должна быть равна 20")
    else:
        # Маскировка банковской карты
        card_name = []
        card_numbers = []
        for i in account_card_split:
            if i.isalpha():
                card_name.append(i)
            elif i.isdigit():
                card_numbers.append(i)

        str_card_name = " ".join(card_name)
        str_card_numbers = "".join(card_numbers)
        if len(str_card_numbers) == 16:
            return str_card_name + " " + get_mask_card_number(str_card_numbers)
        raise ValueError("Длина номера банковской карты должна быть равна 16")


def get_date(date_str: str) -> str:
    """Функция обработки даты"""

    if not date_str:
        raise ValueError("Дата не может быть пустой")

    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise TypeError('Введите дату в корректном формате (например, "2024-03-11" или "2024-03-11T02:26:18")')
