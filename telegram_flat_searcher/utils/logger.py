# teledatastore/teledatastore/logger.py

import logging

def setup_logger(name):
    """
    Настройка логгера для библиотеки.

    Args:
        name (str): Имя логгера.

    Returns:
        logging.Logger: Логгер, настроенный с указанным именем.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Установка уровня логгирования

    # Форматирование сообщений лога
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Настройка вывода лога в консоль
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # Добавление обработчика в логгер
    logger.addHandler(ch)

    return logger
