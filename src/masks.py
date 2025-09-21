import logging
import os

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "masks_logs.log")
masks_logger = logging.getLogger("masks_logger")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""

    masks_logger.info("Запуск функции маскировки номера карты")

    try:
        # Проверяем, что строка состоит только из цифр
        if not number_card.isdigit():
            masks_logger.error("Входные данные имеют неверный формат!")
            raise AttributeError("На номере карты символы отсутствуют, введите числа")

        # Проверяем длину
        if len(number_card) != 16:
            masks_logger.warning("Входные данные не могут быть обработаны корректно!")
            raise ValueError("Длина номера банковской карты должна быть равна 16")

        # Если все проверки пройдены
        masks_logger.info("Маскировка номера карты прошла успешно")
        return number_card[0:4] + " " + number_card[4:6] + "**" + " " + "****" + " " + number_card[-4:]

    except AttributeError as e:
        # Перевызываем то же самое исключение
        masks_logger.error("Входные данные имеют неверный формат!")
        raise AttributeError("На номере карты символы отсутствуют, введите числа") from e


def get_mask_account(number_acc: str) -> str:
    """Функция маскировки номера банковского счета"""

    masks_logger.info("Запуск функции маскировки номера карты")

    try:
        # Проверяем, что строка состоит только из цифр
        if not number_acc.isdigit():
            masks_logger.error("Входные данные имеют неверный формат!")
            raise AttributeError("На номере счета символы отсутствуют, введите числа")

        # Проверяем длину
        if len(number_acc) != 20:
            masks_logger.warning("Входные данные не могут быть обработаны корректно!")
            raise ValueError("Длина номера банковского счета должна быть равна 20")

        # Если все проверки пройдены
        masks_logger.info("Маскировка номера счета прошла успешно")
        return "**" + number_acc[-4:]

    except AttributeError as e:
        # Перевызываем то же самое исключение
        masks_logger.error("Входные данные имеют неверный формат!")
        raise AttributeError("На номере счета символы отсутствуют, введите числа") from e


# Для тестирования
# -------------------------------------------------------------------------------------------------
# if __name__ == "__main__":
#     print(get_mask_card_number("1596837868705199"))
#     print(get_mask_card_number("159683786870519"))
#     print(get_mask_card_number(1596837868705199))
#     print(get_mask_account("12751596837868705199"))
#     print(get_mask_account("15968378687051999999"))
#     print(get_mask_account(1596837868705199))
