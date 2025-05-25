import requests
from dotenv import load_dotenv
import os
from typing import Union, Any, List, Dict
from src.decorators import log

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной API_KEY из .env-файла
API_KEY = os.getenv('API_KEY')


# @log()
def get_amount_transaction(transaction: dict) -> Any:
    """Функция, которая возвращает сумму операции в рублях, конвертируя при необходимости"""

    try:
        amount = transaction.get("operationAmount", {}).get("amount")
        currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency_code != "RUB":
            response_amount = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}&apikey={API_KEY}")
            response_amount.raise_for_status()
            return f"Сумма транзакции в рублях: {response_amount.json()['result']}"
    except AttributeError:
        print("Некорректный тип данных")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса {e}")
    else:
        return f"Сумма транзакции в рублях: {amount}"


print(get_amount_transaction({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD"
        }}}))

# def get_amount_transaction(transaction: dict) -> Any:
#     """Функция, которая возвращает сумму операции в рублях, конвертируя при необходимости"""
#
#     amount = transaction.get("operationAmount", {}).get("amount")
#     currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
#     if currency_code != "RUB":
#         response_amount = requests.get(
#             f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}&apikey={API_KEY}")
#         return f"Сумма транзакции в рублях: {response_amount.json()['result']}"
#     return f"Сумма транзакции в рублях: {amount}"
