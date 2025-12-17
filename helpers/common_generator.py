import random
import string

class CommonGenerator:
    
    @staticmethod
    def generate_random_string(length=10):
        """Генерация случайной строки из букв и цифр"""
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))