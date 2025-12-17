from helpers.common_generator import CommonGenerator


class UserGenerator:
    
    @staticmethod
    def generate_user_data(email=None, password=None, name=None):
        """Генерация данных для создания пользователя"""
        password = password or CommonGenerator.generate_random_string(10)
        return {
            "name": name or CommonGenerator.generate_random_string(10),
            "email": email or f'{CommonGenerator.generate_random_string(10)}@yandex.ru',
            "password": password,
            "submitPassword": password
        }