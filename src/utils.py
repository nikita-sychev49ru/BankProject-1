import json
import logging
import os
from json import JSONDecodeError
from typing import Union

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "utils_logs.log")
utils_logger = logging.getLogger("utils_logger")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_transactions(data_path: Union[str | None] = None) -> list:
    """Функция, которая принимает JSON файл с транзакциями и возвращает список словарей с данными"""

    utils_logger.info("Поиск файла со списком операций")
    if not data_path:
        utils_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(utils_dir, "..", "data", "operations.json")
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            utils_logger.info("Чтение файла со списком операций")
            content = json.load(f)
            if isinstance(content, list):
                utils_logger.info("Список операций успешно сформирован")
                return content
            else:
                utils_logger.warning("Файл содержит некорректные данные!")
                return []
    except (ValueError, JSONDecodeError, TypeError):
        utils_logger.error("Файл не может быть прочитан!")
        return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден!")
        return []


# Для тестирования
# ---------------------------------------------------------------------------------------------------------------
# utils_dir = os.path.dirname(__file__)
# data_path = os.path.join(utils_dir, "..", "data", "operations.json")
# if __name__ == "__main__":
#     operations1 = get_transactions()
#     operations2 = get_transactions(data_path)
#     operations3 = get_transactions(
#         os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "data_for_example.txt")
#     )
#     operations4 = get_transactions((os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data",
#     "le.json")))
#
#     print(f"Загружено операций: {len(operations1)}, {len(operations2)}, {len(operations3)}, {len(operations4)}")
