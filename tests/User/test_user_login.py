import allure
from helpers.user_generator import UserGenerator
from helpers.api_client import ApiClient
from config.error_messages import AssertMessages


@allure.suite("Авторизация")
class TestUserLogin:
    
    @allure.epic("User API")
    @allure.feature("Авторизация пользователя")
    @allure.title("Авторизация пользователя: позитивный кейс")
    @allure.description("Тест проверяет успешную авторизацию существующего пользователя")
    def test_user_login(self):
        with allure.step("Подготовить тестовые данные"):
            payload = UserGenerator.register_new_user()
        
        with allure.step("Отправить запрос на авторизацию пользователя"):
            response = ApiClient.post_request_login_user(payload)
        
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 201, (
                AssertMessages.STATUS_CODE_MISMATCH.format(expected=201, actual=response.status_code)
            )
        
        with allure.step("Проверить наличие access_token в ответе"):
            response_data = response.json()
            assert 'token' in response_data, AssertMessages.FIELD_MISSING.format(field_name='token')
            assert 'access_token' in response_data['token'], AssertMessages.FIELD_MISSING.format(field_name='access_token')