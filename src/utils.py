from typing import Union, Any, List, Dict
import json
import os


def get_transactions(filepath: str) -> list[Any] | None | Any:
    """Функция, которая принимает JSON файл и возвращает список словарей с данными"""

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
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


utils_dir = os.path.dirname(__file__)
data_path = os.path.join(utils_dir, "..", "data", "operations.json")
print(get_transactions(data_path))
