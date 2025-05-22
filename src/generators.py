from typing import Any, Dict, Generator, List


def filter_by_currency(transactions_list: List, currency: str) -> Any:
    """Генератор для выдачи транзакций, где валюта операции соответствует заданной(например, USD)"""

    if not transactions_list:
        yield "Отсутствуют данные!"
    elif not any(
        transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        for transaction in transactions_list
    ):
        yield "Транзакции с данной валютой отсутствуют"
    else:
        yield from (
            transaction
            for transaction in transactions_list
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        )


def transaction_descriptions(transactions_list: List[Dict]) -> Generator[str | None | Any, Any, None]:
    """Генератор, который возвращает описание каждой операции по очереди"""

    if not transactions_list:
        yield "Отсутствуют данные!"
    else:
        yield from (
            transaction.get("description", "Отсутствует описание транзакции") for transaction in transactions_list
        )


def card_number_generator(start: int, stop: int) -> Any:
    """Генератор номеров банковских карт"""

    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Неверный формат данных!")
    elif start <= 0 or len(str(start)) > 16 or len(str(stop)) > 16:
        raise ValueError("Ошибка при вводе значений границ диапазона!")
    elif start >= stop:
        raise ValueError("Ошибка: начальное значение должно быть меньше конечного!")
    else:
        for number in range(start, stop + 1):
            card_num = str(number).zfill(16)
            yield " ".join([card_num[i : i + 4] for i in range(0, 16, 4)])
