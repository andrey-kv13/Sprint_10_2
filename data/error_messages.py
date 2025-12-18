"""Константы с сообщениями об ошибках API"""


class ErrorMessages:
    """Сообщения об ошибках API"""
    EMAIL_ALREADY_IN_USE = "Почта уже используется"


class AssertMessages:
    """Шаблоны сообщений для assert"""
    
    # Статус код
    STATUS_CODE_MISMATCH = "Ожидался статус код {expected}, получен {actual}"
    
    # Сообщения об ошибках
    ERROR_MESSAGE_MISMATCH = "Ожидалось сообщение: '{expected}', получено: '{actual}'"
    
    # Поля данных
    FIELD_MISSING = "В ответе отсутствует поле {field_name}"
    FIELD_VALUE_MISMATCH = "Ожидалось {field_name}: '{expected}', получено: '{actual}'"
