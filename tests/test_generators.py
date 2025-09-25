import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected",
                         [("USD", "Отсутствуют данные для обработки"), ("RUB", "Отсутствуют данные для обработки")])
def test_filter_by_currency_empty(transactions_empty: list, currency: str, expected: list) -> None:
    """Тест на пустой список транзакций"""

    result = "".join(filter_by_currency(transactions_empty, currency))
    assert result == expected


@pytest.mark.parametrize(
    "currency, expected",
    [("EUR", "В списке отсутствуют транзакции с данной валютой"), ("BTC", "В списке отсутствуют транзакции с данной валютой")],
)
def test_filter_by_currency_not_code(transactions: list, currency: str, expected: list) -> None:
    """Тест на отсутствие заданной валюты"""

    result = "".join(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
                "USD",
                [{'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'amount': '8221.37',
                  'currency_name': 'USD', 'currency_code': 'USD', 'from': 'MasterCard 7158300734726758',
                  'to': 'Счет 35383033474447895560', 'description': 'Перевод организации'},
                 {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'amount': '9824.07',
                  'currency_name': 'USD', 'currency_code': 'USD', 'from': 'Счет 75106830613657916952',
                  'to': 'Счет 11776614605963066702', 'description': 'Перевод организации'},
                 {'id': '142264268', 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'amount': '79114.93',
                  'currency_name': 'USD', 'currency_code': 'USD', 'from': 'Счет 19708645243227258542',
                  'to': 'Счет 75651667383060284188', 'description': 'Перевод со счета на счет'}],
        )
    ],
)
def test_filter_by_currency(transactions: list, currency: str, expected: list) -> None:
    """Тест на корректную фильтрацию по заданной валюте"""

    assert list(filter_by_currency(transactions, currency)) == expected


def test_transaction_descriptions_empty() -> None:
    """Тест на пустой список транзакций"""

    assert list(transaction_descriptions([])) == ["Отсутствуют данные!"]


def test_transaction_descriptions_or_not(transaction_descriptions_or_not: list) -> None:
    """Тест для функции получения описаний транзакций -
    в одном из словарей отсутствует ключ "description" """

    result = list(transaction_descriptions(transaction_descriptions_or_not))
    assert result == ["Отсутствует описание транзакции", "Перевод со счета на счет"]


def test_transaction_descriptions(transactions: list, transaction_descriptions_list: list) -> None:
    """Тест на возвращение корректных описаний для каждой транзакции"""

    assert list(transaction_descriptions(transactions)) == transaction_descriptions_list


@pytest.mark.parametrize(
    "start, stop, expected", [(1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])]
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """Тест для корректной обработки номеров банковских карт"""

    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_start_more() -> None:
    """Тест для обработки, если начало диапазона больше, чем конец"""

    with pytest.raises(ValueError, match="Ошибка: начальное значение должно быть меньше конечного!"):
        list(card_number_generator(6, 4))


def test_card_number_generator_zero() -> None:
    """Тест для обработки, если начало диапазона меньше нуля"""

    with pytest.raises(ValueError, match="Ошибка при вводе значений границ диапазона!"):
        list(card_number_generator((-6), 4))


def test_card_number_generator_is_not_digit() -> None:
    """Тест для обработки, если введено нецифровое значение"""

    with pytest.raises(TypeError, match="Неверный формат данных!"):
        list(card_number_generator("1", 4))


def test_card_number_generator_start_stop() -> None:
    """Тест для обработки, если начало и конец диапазона совпадают"""

    with pytest.raises(ValueError, match="Ошибка: начальное значение должно быть меньше конечного!"):
        list(card_number_generator(4, 4))
