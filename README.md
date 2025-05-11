# Проект "Сбербанк на минималках"

## Описание:

Данный проект - это MVP приложения банка, которое будет помогать пользователям проводить операции между банковскими счетами, проводить аналитику своих счетов, распределять бюджет. Проект достаточно сырой, но постепенно развивается. Впоследствии данный документ будет обновляться информацией. 

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/nikita-sychev49ru/BankProject-1.git
```

2. Добавление линтеров:
```
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

## Использование:

1. Функция `get_mask_card_number`, предназначена для маскировки банковской карты
2. Функция `get_mask_account`, предназначена для маскировки номера банковского счета
3. Функция `mask_account_card`, доработанная версия предыдущих функций, предназначена для опциональной проверки, и маскировки карты или счета пользователя, в зависимости от того, что мы получаем на вход
4. Функция `get_date`, используется для обработки даты в удобном формате для пользователского восприятия
5. Функция `filter_by_state`, предназначена для фильтрации обработки операций пользователей, обрабатывается по заданному ключу
6. Функция `sort_by_date`, сортирует операции по датам, по умолчанию - по возрастанию

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

Фикстуры содержатся в файле `conftest.py` проекта. 

## Лицензия:

Пока без лицензии.
