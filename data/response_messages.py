"""Ожидаемые сообщения в ответах API"""


class SuccessMessages:
    """Сообщения об успешных операциях"""
    LISTING_DELETED = "Объявление удалено успешно"


class ErrorResponseMessages:
    """Сообщения об ошибках в ответах API"""
    TOKEN_INVALID = "Токен не действителен"
    LISTING_NOT_FOUND_OR_NO_PERMISSION = "Оффер не найден или у вас нет прав на его редактирование"
