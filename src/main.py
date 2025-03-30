from masks import get_mask_account, get_mask_card_number
from widget import mask_account_card

# # Пользователь вводит номер карты и получает ее маску
# print(get_mask_card_number(input("Введите номер карты (16 цифр): ")))
#
# # Пользователь вводит номер счета и получает его маску
# print(get_mask_account(input("Введите номер счета (20 цифр): ")))

#Пользователь вводит номер счет или карты и получает маску
print(mask_account_card(input("Введите банковский продукт: ")))
