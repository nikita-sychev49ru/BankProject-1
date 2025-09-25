import csv
import os
from typing import Any

import pandas as pd


def get_transactions_csv(file_path: str | None = None) -> Any:
    """Функция считывает операции из csv файла и возвращает список словарей"""

    if not file_path:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(utils_dir, "..", "data", "transactions.csv")

    try:
        list_transactions_csv = []
        with open(file_path, "r", encoding="utf-8") as file:
            content = csv.DictReader(file, delimiter=";")
            for row in content:
                list_transactions_csv.append(row)
            if len(list_transactions_csv) != 0:
                return list_transactions_csv
            else:
                print("Данные некорректны!")
    except FileNotFoundError:
        print("Файл не найден!")


def get_transactions_xlsx(file_path: str | None = None) -> Any:
    """Функция считывает операции из xlsx файла и возвращает список словарей"""

    if not file_path:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(utils_dir, "..", "data", "transactions_excel.xlsx")
    try:
        content = pd.read_excel(file_path)
        content_xlsx = content.to_dict(orient="records")
        return content_xlsx
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception:
        print("Данные некорректны!")


# Для тестирования

# utils_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(utils_dir, "..", "data", "transactions_excel.xlsx")
#
# if __name__ == "__main__":
#     x = get_transactions_csv()
#     print(x[0])
#     print('------------------------------')
#     y = get_transactions_xlsx()
#     print(y[0])
