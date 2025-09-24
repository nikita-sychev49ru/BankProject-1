import re
from collections import Counter
from typing import Any

import pandas as pd

from src.tables_reading import get_transactions_csv, get_transactions_xlsx
from src.utils import get_transactions


def get_transactions_optional_format() -> list | str:
    """Функция, которая отвечает за опциональное получение информации
    о транзакциях из источников разного формата .csv, .xlsx, .json"""

    file_format = input(
        """Выберите необходимый формат:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    => """
    )
    if file_format == "1":
        print("Для обработки выбран JSON-файл.")
        transaction_list = get_transactions()
        transactions = []
        for item in transaction_list:
            transaction = normalize_transaction(item)
            transactions.append(transaction)
        return transactions
    elif file_format == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = get_transactions_csv()
        return transactions
    elif file_format == "3":
        print("Для обработки выбран XLSX-файл.")
        transaction_list = get_transactions_xlsx()
        transactions = []
        for item in transaction_list:
            transaction = normalize_transaction(item)
            transactions.append(transaction)
        return transactions
    else:
        return "Ошибка ввода! Данные не найдены!"


def normalize_transaction(transaction: Any) -> dict:
    """Приводит транзакцию из любого формата к единому виду"""

    normalized = {
        "id": None,
        "state": None,
        "date": None,
        "amount": None,
        "currency_name": None,
        "currency_code": None,
        "from": None,
        "to": None,
        "description": None,
    }

    # Обработка JSON формата
    if "operationAmount" in transaction:
        normalized["id"] = str(transaction.get("id"))
        normalized["state"] = transaction.get("state")
        normalized["date"] = str(transaction.get("date"))

        # Обрабатываем вложенные словари amount, currency
        op_amount = transaction.get("operationAmount", {})
        normalized["amount"] = str(op_amount.get("amount", "0"))
        currency = op_amount.get("currency", {})
        normalized["currency_name"] = currency.get("name")
        normalized["currency_code"] = currency.get("code")

        normalized["from"] = transaction.get("from")
        normalized["to"] = transaction.get("to")
        normalized["description"] = transaction.get("description")

    # Обработка XLSX формата
    else:
        normalized["id"] = str(transaction.get("id")) if transaction.get("id") else ""
        normalized["state"] = transaction.get("state")
        normalized["date"] = transaction.get("date")

        # Для amount: преобразуем в str, независимо от исходного типа
        amount = transaction.get("amount")
        if amount is not None:
            normalized["amount"] = str(amount)
        else:
            normalized["amount"] = "0"

        normalized["currency_name"] = transaction.get("currency_name")
        normalized["currency_code"] = transaction.get("currency_code")
        normalized["from"] = transaction.get("from")
        normalized["to"] = transaction.get("to")
        normalized["description"] = transaction.get("description")

    return normalized


def search_transactions(transactions: Any = None, target: Any = None) -> list:
    """Функция принимает список словарей с данными о банковских
       операциях и строку поиска, а возвращает список словарей,
       у которых в описании есть данная строка"""

    if not transactions or not target:
        transactions, target = get_transactions_optional_format(), input("Введите слово для поиска: ")

    try:
        filtered_transactions = []
        pattern_search = re.compile(re.escape(str(target)), flags=re.IGNORECASE)

        for transaction in transactions:
            for value in transaction.values():
                if value and isinstance(value, str) and pattern_search.search(value):
                    filtered_transactions.append(transaction)
                    break
        return filtered_transactions
    except TypeError("Слово для поиска имеет неверный формат"):
        return []


def get_count_category(transactions: Any, categories: list) -> dict:
    """Функция принимает список банковских операций и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории."""

    df_transactions = pd.DataFrame(transactions)
    stat_information = dict(Counter(df_transactions["description"]))
    stat_information_by_categories = {k: v for k, v in stat_information.items() if k in categories}
    for category in categories:
        if category not in stat_information_by_categories:
            stat_information_by_categories[category] = 0
    return stat_information_by_categories
