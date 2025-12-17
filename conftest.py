import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers.listing_generator import ListingGenerator
from helpers.user_generator import UserGenerator
from helpers.api_client import ApiClient

@pytest.fixture
def register_new_user():
    """Фикстура: регистрирует нового пользователя и возвращает (payload, headers)"""
    payload = UserGenerator.generate_user_data()
    response = ApiClient.post_request_create_user(payload)
    if response.status_code != 201:
        pytest.fail(f"Failed to register user: {response.text}")
    
    response_data = response.json()
    auth_token = response_data['access_token']['access_token']
    headers = {"Authorization": f"Bearer {auth_token}"}
    return payload, headers


@pytest.fixture(scope="session")
def register_and_login_user():
    """Фикстура для регистрации и авторизации пользователя"""
    payload = UserGenerator.generate_user_data()
    response = ApiClient.post_request_create_user(payload)
    if response.status_code != 201:
        pytest.fail(f"Failed to register user: {response.text}")
    
    response_data = response.json()
    auth_token = response_data['access_token']['access_token']
    headers = {"Authorization": f"Bearer {auth_token}"}
    
    response = ApiClient.post_request_login_user(payload)
    if response.status_code != 201:
        pytest.fail(f"Failed to login user: {response.text}")
    
    return payload, headers


@pytest.fixture
def created_listing(register_and_login_user):
    """Фикстура: создаёт объявление и возвращает его данные"""
    _, headers = register_and_login_user
    payload = ListingGenerator.generate_listing_data()
    response = ApiClient.post_request_create_listing(headers, payload)
    
    return {
        "listing_id": response.json()['id'],
        "original_price": response.json()['price'],
        "owner_headers": headers
    }
