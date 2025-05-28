# Проект "Сбербанк на минималках"

## Описание:

Данный проект - это MVP приложения банка, которое будет помогать пользователям проводить операции между банковскими счетами, проводить аналитику своих счетов, распределять бюджет. Проект достаточно сырой, но постепенно развивается. Впоследствии данный документ будет обновляться информацией. 

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/nikita-sychev49ru/BankProject-1.git
```

2. Добавление линтеров и библиотек:
```
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
poetry add requests
poetry add python-dotenv

```

## Использование:

1. Функция `get_mask_card_number`, предназначена для маскировки банковской карты
2. Функция `get_mask_account`, предназначена для маскировки номера банковского счета
3. Функция `mask_account_card`, доработанная версия предыдущих функций, предназначена для опциональной проверки, и маскировки карты или счета пользователя, в зависимости от того, что мы получаем на вход
4. Функция `get_date`, используется для обработки даты в удобном формате для пользовательского восприятия
5. Функция `filter_by_state`, предназначена для фильтрации обработки операций пользователей, обрабатывается по заданному ключу
6. Функция `sort_by_date`, сортирует операции по датам, по умолчанию - по возрастанию
7. Функция `filter_by_currency`, предназначена для фильтрации списка транзакций, обрабатывается по заданной валюте
8. Функция `transaction_descriptions`, возвращает описание по каждой из транзакций
9. Функция `card_number_generator`, генератор номеров банковских карт, который создает номера в заданном диапазоне и возвращает их в формате XXXX XXXX XXXX XXXX
10. Функция `log`, декоратор, который фиксирует запуск других функций, передаваемые при запуске аргументы, вычисляет время исполнения, результаты, сообщает сведения об ошибках, если они возникли при выполнении. Может выводить полученные данные в консоль или записывать в файл
11. Функция `get_transactions`, принимает JSON файл с транзакциями и возвращает список словарей с данными
12. Функция `get_amount_transaction`, возвращает сумму операции в рублях, конвертируя при необходимости, обращаясь к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли
## Примеры использования функция:

1. **`sort_by_date` - возвращает отсортированный список по датам**
```
   def sort_by_date(operations: list[dict], sort: bool = True) -> list[dict]:
    """Функция сортировки операций по дате"""

    sorted_operations = sorted(operations, key=lambda item: item["date"], reverse=sort)
    return sorted_operations


    test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

   print(sort_by_date(test_list))
```
2. **`filter_by_state` - возвращает отсортированный список операций по заданному ключу**
```
  def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по ключу"""

    list_operations = []
    for i in operations:
        if state in i["state"]:
            list_operations.append(i)
    return list_operations

  test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

  print(filter_by_state(test_list))
```
3. **`mask_account_card` - маскирует карту или счет пользователя c использованием внутри себя двух функций `get_mask_account` и `get_mask_card_number`**
```
  def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""

    return number_card[0:4] + " " + number_card[4:6] + "**" + " " + "****" + " " + number_card[-4:]


def get_mask_account(number_acc: str) -> str:
    """Функция маскировки номера банковского счета"""

    return "**" + number_acc[-4:]
```

  Далее проверяем маскировку, используя `mask_account_card`
  ```
    from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты и счета"""

    account_card_split = account_card.split()

    # Маскировка счета
    if "Счет" in account_card_split:
        return f"Счет {get_mask_account(account_card_split[1])}"
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
        return str_card_name + " " + get_mask_card_number(str_card_numbers)

        print(mask_account_card(input("Введите банковский продукт: ")))
  ```

4. `get_date` - обрабатываем дату и выдаем пользователю в удобночитаемом формате
  ```
  from datetime import datetime
  
  def get_date(date_str: str) -> str:
    """Функция обработки даты"""

    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

    print(get_date(input("Введите дату в формате(2024-03-11T02:26:18.671407): ")))
  ```

5. `filter_by_currency` - фильтруем транзакции по заданной валюте
```
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
```
6. `transaction_descriptions` - описание типов транзакций
```
def transaction_descriptions(transactions_list: List[Dict]) -> Generator[str | None | Any, Any, None]:
    """Генератор, который возвращает описание каждой операции по очереди"""

    if not transactions_list:
        yield "Отсутствуют данные!"
    else:
        yield from (
            transaction.get("description", "Отсутствует описание транзакции") for transaction in transactions_list
        )
```
7. `card_number_generator` - генератор номеров банковских карт
```
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
```
## Тестирование:


1. Установка `pytest` и библиотеку `pytest-cov`
``` 
poetry add --group dev pytest
poetry add --group dev pytest-cov
```
2.  `test_get_mask_card_number` - функция, которая тестирует маскировку карты, дополнительно обрабатывает исключения, в случае некорректного ввода.
3.  `test_get_mask_account` - функция, которая тестирует маскировку счета, дополнительно обрабатывает исключения, в случае некорректного ввода.
4.  `test_mask_account_card` - функция, которая тестирует опциональную маскировку счета или карты, дополнительно проверяет длину и корректность ввода вне зависимости от регистра
5.  `test_mask_account_card_empty` - функция, которая тестирует заполненность списка карты или счета
6.  `test_get_date_valid` и `test_get_date_invalid` - функция, которая тестирует дату на валидность
7.  `test_get_date_empty` - функция, которая тестирует на заполненность даты
8.  `test_filter_by_state` - функция, которая тестирует фильтрацию обработки операций пользователей с использованием фикстур в параметризации
9.  `test_empty_list_by_state` - функция, которая тестирует заполненность списка операций пользователей
10.  `test_sort_by_date` - функция, которая тестирует сортировку операций с разными датами
11.  `test_sort_with_same_dates` - функция, которая тестирует исходный порядок с одинаковыми датами
12.  `test_empty_list_date` - функция, которая тестирует заполненность списка с датами операций
13.  `test_missing_date_key` - функция, которая тестирует список с отсутствующим ключом `date`
14.  `test_invalid_date_format` - функция, которая тестирует некорректный формат даты
15.  `test_filter_by_currency_empty` - функция, которая тестирует заполненность списка транзакций
16.  `test_filter_by_currency_not_code` - функция, которая тестирует отсутствие заданной валюты
17.  `test_filter_by_currency` - функция, которая тестирует корректную фильтрацию по заданной валюте
18.  `test_transaction_descriptions_empty` - функция, которая тестирует на заполненность списка транзакций для вывода описаний
19.  `test_transaction_descriptions_or_not` - функция, которая тестирует отсутствие ключа `description` одной из транзакций
20.  `test_transaction_descriptions` - функция, которая тестирует корректное возвращение описаний по каждой транзакции
21.  `test_card_number_generator` - функция, которая тестирует корректную обработку номеров банковских карт
22.  `test_card_number_generator_start_more` - функция, которая тестирует, если начала диапазона больше, чем конец
23.  `test_card_number_generator_zero` - функция, которая тестирует, если начало диапазона меньше нуля
24.  `test_card_number_generator_is_not_digit` - функция, которая тестирует формат данных, если введено нецифровое значение
25.  `test_card_number_generator_start_stop` - функция, которая тестирует совпадение начала и конца диапазона
26.  `test_log_normal_console` - функция, которая тестирует успешную отработку декоратора `log` для вывода в консоль
27.  `test_log_error_console` - функция, которая тестирует наличие ошибок декоратора `log` для вывода в консоль
28.  `test_log_normal_file` - функция, которая тестирует успешную отработку декоратора `log` для записи в файл
29.  `test_log_error_file` - функция, которая тестирует наличие ошибок декоратора `log` для записи в файл

Фикстуры содержатся в файле `conftest.py` проекта. 
Данные с банковскими операциями содержатся в файле `operations.json`
## Лицензия:

Пока без лицензии.
