from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest


@pytest.mark.parametrize(
    "currency, expected", [("USD", "Отсутствуют данные!"), ("RUB", "Отсутствуют данные!")]
)
def test_filter_by_currency_empty(transactions_empty: list, currency: str, expected: list) -> None:
    """Тест на пустой список транзакций"""

    result = "".join(filter_by_currency(transactions_empty, currency))
    assert result == expected


@pytest.mark.parametrize(
    "currency, expected",
    [("EUR", "Транзакции с данной валютой отсутствуют"), ("BTC", "Транзакции с данной валютой отсутствуют")]
)
def test_filter_by_currency_not_code(transactions: list, currency: str, expected: list) -> None:
    """Тест на отсутствие заданной валюты"""

    result = "".join(filter_by_currency(transactions, currency))
    assert result == expected


@pytest.mark.parametrize('currency, expected', [(
        'USD', [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                 'to': 'Счет 11776614605963066702'},
                {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                 'to': 'Счет 75651667383060284188'},
                {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
                 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
                 'to': 'Visa Platinum 8990922113665229'}]
)])
def test_filter_by_currency(transactions, currency, expected) -> None:
    """Тест на корректную фильтрацию по заданной валюте"""

    assert list(filter_by_currency(transactions, currency)) == expected


def test_transaction_descriptions_empty():
    """Тест на пустой список транзакций"""

    assert list(transaction_descriptions([])) == ['Отсутствуют данные!']


def test_transaction_descriptions_or_not(transaction_descriptions_or_not: list) -> None:
    """Тест для функции получения описаний транзакций -
    в одном из словарей отсутствует ключ "description" """

    result = list(transaction_descriptions(transaction_descriptions_or_not))
    assert result == ['Отсутствует описание транзакции', 'Перевод со счета на счет']


def test_transaction_descriptions(transactions: list, transaction_descriptions_list: list) -> None:
    """Тест на возвращение корректных описаний для каждой транзакции"""

    assert list(transaction_descriptions(transactions)) == transaction_descriptions_list


@pytest.mark.parametrize('start, stop, expected',
                         [(1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003'])])
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """Тест для корректной обработки номеров банковских карт"""

    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_stop_more() -> None:
    """Тест для обработки, если начало диапазона меньше, чем конец"""

    with pytest.raises(ValueError, match="Ошибка: начальное значение должно быть меньше конечного!"):
        list(card_number_generator(6, 4))


def test_card_number_generator3() -> None:
    """Тест для обработки, если начало диапазона меньше нуля"""

    with pytest.raises(ValueError, match="Ошибка при вводе значений границ диапазона!"):
        list(card_number_generator((-6), 4))


def test_card_number_generator4() -> None:
    """Тест для обработки, если введено нецифровое значение"""

    with pytest.raises(TypeError, match="Неверный формат данных!"):
        list(card_number_generator("1", 4))


def test_card_number_generator6() -> None:
    """Тест для обработки, если начало и конец диапазона совпадают"""

    with pytest.raises(ValueError, match="Ошибка: начальное значение должно быть меньше конечного!"):
        list(card_number_generator(4, 4))
