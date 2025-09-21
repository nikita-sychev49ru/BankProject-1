import json
import logging
import os
from json import JSONDecodeError
from typing import Any


log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "utils_logs.log")
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_transactions(filepath: str) -> list[Any] | None | Any:
    """Функция, которая принимает JSON файл с транзакциями и возвращает список словарей с данными"""

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
    else:
        if isinstance(content, list) and len(content) > 0:
            return content
        else:
            return []


# Для тестирования
utils_dir = os.path.dirname(__file__)
data_path = os.path.join(utils_dir, "..", "data", "operations.json")
print(get_transactions(data_path))
