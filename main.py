from typing import List, Dict, Any, Iterator
# from src.utils import transactions_dict










# def filter_by_currency(transactions_list: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
#     """Фильтрует транзакции по заданной валюте и возвращает итератор."""
#     # Проверка типа входных данных
#     if not isinstance(transactions_list, list):
#         raise ValueError("Ожидается список транзакций.")
#
#     if not isinstance(currency, str):
#         raise ValueError("Ожидается строка для валюты.")
#
#     for transaction in transactions_list:
#         # Проверяем, что каждая транзакция является словарем
#         if not isinstance(transaction, dict):
#             raise ValueError("Каждая транзакция должна быть словарем.")
#         # Проверяем, содержит ли транзакция ключ 'currency'
#         if "currency" not in transaction["operationAmount"]:
#              raise ValueError("Каждая транзакция должна содержать ключ 'currency'.")
#         if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
#             yield transaction
#
# try:
#     usd_transactions = filter_by_currency(transactions, 'USD')
#     for transaction in usd_transactions:
#         print(transaction)
#
# except ValueError as e:
#      print(f"Ошибка: {e}")

