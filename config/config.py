class Config:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/api"

    """Ручки для взаимодействия с пользователем"""
    USER_CREATE_URL = f"{BASE_URL}/signup"
    USER_LOGIN_URL = f"{BASE_URL}/signin"
    
    """Ручки для взаимодействия с объявлениями"""
    LISTING_CREATE_URL = f"{BASE_URL}/create-listing"
    LISTING_UPDATE_URL = f"{BASE_URL}/update-offer/{{}}"  # {} для .format(id)
    LISTING_DELETE_URL = f"{BASE_URL}/listings/{{}}"  # {} для .format(id)