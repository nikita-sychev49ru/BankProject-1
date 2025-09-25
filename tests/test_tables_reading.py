import os
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.tables_reading import get_transactions_csv, get_transactions_xlsx


def test_get_transactions_csv1(make_csv_transaction: dict) -> None:
    """Тест для функции, считывающей транзакции из файла .csv - норма"""
    csv_content = """id;state;date
650703;EXECUTED;2023-09-05T11:30:32Z"""
    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = get_transactions_csv()
    assert result == make_csv_transaction


def test_get_transactions_csv2(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции, считывающей транзакции из файла .csv -
    данные не являются словарем"""
    csv_content = """date"""
    expect_result = "Данные некорректны!"
    with patch("builtins.open", mock_open(read_data=csv_content)):
        get_transactions_csv()
        print_result = capsys.readouterr()
    assert print_result.out.strip() == expect_result


def test_get_transactions_csv3(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции, считывающей транзакции из файла .csv -
    файл или папка не найдены"""
    get_transactions_csv("../date/transactions.csv")
    print_result = capsys.readouterr()
    expect_result = "Файл не найден!"
    assert print_result.out.strip() == expect_result


def test_get_transactions_csv4(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции, считывающей транзакции из файла .csv -
    файл имеет формат, отличный от .csv"""
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, "..", "data", "example.json")
    get_transactions_csv(file_path)
    print_result = capsys.readouterr()
    expect_result = "Файл не найден!"
    assert print_result.out.strip() == expect_result


def test_get_transactions_xlsx1() -> None:
    """Тест для функции, считывающей транзакции из файла .xlsx - норма"""
    data_frame = pd.DataFrame({"name": ["Ann", "Bob"], "age": [25, 31], "city": ["NY", "LA"]})
    with patch("pandas.read_excel", return_value=data_frame):
        result = get_transactions_xlsx()
    assert result[0] == {"name": "Ann", "age": 25, "city": "NY"}


def test_get_transactions_xlsx2(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции, считывающей транзакции из файла .xlsx -
    файл или папка не найдены"""
    get_transactions_xlsx("../date/transactions_excel.xlsx")
    print_result = capsys.readouterr()
    expect_result = "Файл не найден!"
    assert print_result.out.strip() == expect_result


def test_get_transactions_xlsx3(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для функции, считывающей транзакции из файла .xlsx -
    файл имеет формат, отличный от .xlsx"""
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(file_dir, "..", "data", "example.json")
    get_transactions_xlsx(file_path)
    print_result = capsys.readouterr()
    expect_result = "Файл не найден!"
    assert print_result.out.strip() == expect_result
