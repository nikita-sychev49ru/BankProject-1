import os
import tempfile

import pytest

from src.decorators import log


def test_log_normal_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для декоратора log - вывод в консоль (Успешная отработка функции)"""

    @log(filename=None)
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    captured = capsys.readouterr()
    output = captured.out.split("\n")

    assert "Функция add выполнена успешно." in output[1]
    assert "Входные параметры: ((2, 3), {})" in output[3]
    assert "Результат: 5" in output
    assert result == 5  # Проверяем возвращаемое значение


def test_log_error_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест для декоратора log - вывод в консоль (Ошибка)"""

    @log(filename=None)
    def add(x: int, y: int) -> int:
        return x + y

    add("2", 3)
    captured = capsys.readouterr()
    output = captured.out.split("\n")

    assert "Функция add выполнена безуспешно, возникла ошибка!" in output[1]
    assert "Тип ошибки: <class 'TypeError'>, can only concatenate str (not \"int\") to str" in output[3]
    assert "Входные параметры: (('2', 3), {})" in output[4]


def test_log_normal_file() -> None:
    """Тест для декоратора log - запись в файл (Успешная отработка функции)"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
    try:

        @log(filename=filename)
        def add_nums(x: int, y: int) -> int:
            return x + y

        add_nums(2, 3)
        with open(filename, "r", encoding="utf-8") as file:
            result = file.readlines()
            assert result[1] == "Функция add_nums выполнена успешно.\n"
            assert result[3] == "Входные параметры: ((2, 3), {})\n"
            assert result[4] == "Результат: 5\n"

    finally:
        if os.path.exists(filename):
            os.remove(filename)


def test_log_error_file() -> None:
    """Тест для декоратора log - запись в файл (Ошибка)"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name
    try:

        @log(filename=filename)
        def add_nums(x: int, y: int) -> int:
            return x + y

        add_nums("2", 3)
        with open(filename, "r", encoding="utf-8") as file:
            result = file.readlines()
            assert result[1] == "Функция add_nums выполнена безуспешно, возникла ошибка!\n"
            assert result[3] == "Тип ошибки: <class 'TypeError'>, can only concatenate str (not \"int\") to str\n"
            assert result[4] == "Входные параметры: (('2', 3), {})\n"

    finally:
        if os.path.exists(filename):
            os.remove(filename)
