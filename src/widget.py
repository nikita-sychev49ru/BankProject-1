from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты и счета"""

    account_card_split = account_card.split()

    #Маскировка счета
    if 'Счет' in account_card_split:
        return f"Счет {get_mask_account(account_card_split[1])}"
    else:
        #Маскировка банковской карты
        card_name = []
        card_numbers = []
        for i in account_card_split:
            if i.isalpha():
                card_name.append(i)
            elif i.isdigit():
                card_numbers.append(i)

        str_card_name = " ".join(card_name)
        str_card_numbers = "".join(card_numbers)
        return str_card_name + " " + get_mask_card_number(str_card_numbers)




