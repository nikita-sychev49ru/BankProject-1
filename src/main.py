from masks import get_mask_account, get_mask_card_number

# Пользователь вводит номер карты и получает ее маску
print(get_mask_card_number(input("Введите номер карты (16 цифр): ")))

# Пользователь вводит номер счета и полуает его маску
print(get_mask_account(input("Введите номер счета (20 цифр): ")))
