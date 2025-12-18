from helpers.common_generator import CommonGenerator

class ListingGenerator:
    @staticmethod
    def generate_listing_data(name=None, category=None, condition=None, city=None, description=None, price=None):
        """Генерация данных для создания объявления (multipart/form-data)"""
        return {
            "name": name or CommonGenerator.generate_random_string(10),
            "category": category or "Авто",
            "condition": condition or "Новый",
            "city": city or "Москва",
            "description": description or CommonGenerator.generate_random_string(50),
            "price": price or "1000"
        }  