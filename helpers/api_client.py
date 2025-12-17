import requests
from config.config import Config
from requests_toolbelt import MultipartEncoder


class ApiClient:

    """USER_REQUESTS"""
    @staticmethod
    def post_request_create_user(payload):
        """Создание пользователя"""
        return requests.post(Config.USER_CREATE_URL, json=payload)
    
    @staticmethod
    def post_request_login_user(payload):
        """Авторизация пользователя"""
        return requests.post(Config.USER_LOGIN_URL, json=payload)

    """LISTING_REQUESTS"""
    @staticmethod
    def post_request_create_listing(headers, data, image_path=None):
        """
        Создание объявления с multipart/form-data используя MultipartEncoder
        
        Args:
            headers: заголовки с токеном авторизации
            data: словарь с текстовыми полями (name, category, condition, city, description, price)
            image_path: путь к файлу изображения (опционально)
        """
        fields = data.copy()
        
        if image_path:
            fields['image'] = (image_path.split('/')[-1], open(image_path, 'rb'), 'image/jpeg')
        
        multipart_data = MultipartEncoder(fields=fields)
        
        request_headers = headers.copy()
        request_headers['Content-Type'] = multipart_data.content_type
        
        return requests.post(Config.LISTING_CREATE_URL, headers=request_headers, data=multipart_data)
    
    @staticmethod
    def patch_request_update_listing(headers, listing_id, data, image_path=None):
        """
        Обновление объявления с multipart/form-data
        
        Args:
            headers: заголовки с токеном авторизации
            listing_id: ID объявления для обновления
            data: словарь с текстовыми полями (name, category, condition, city, description, price)
            image_path: путь к файлу изображения (опционально)
        """
        files = {key: (None, value) for key, value in data.items()}
        
        if image_path:
            files['image'] = (image_path.split('/')[-1], open(image_path, 'rb'), 'image/jpeg')
        
        url = Config.LISTING_UPDATE_URL.format(listing_id)
        return requests.patch(url, headers=headers, files=files)
    
    @staticmethod
    def delete_request_delete_listing(headers, listing_id):
        """Удаление объявления"""
        url = Config.LISTING_DELETE_URL.format(listing_id)
        return requests.delete(url, headers=headers)