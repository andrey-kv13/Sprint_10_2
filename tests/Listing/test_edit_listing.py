import allure
from helpers.listing_generator import ListingGenerator
from helpers.api_client import ApiClient
from data.error_messages import AssertMessages
from data.response_messages import ErrorResponseMessages


class TestEditListing:
    
    @allure.epic("Listing API")
    @allure.feature("Редактирование объявления")
    @allure.title("Редактирование объявления: позитивный кейс (владелец)")
    @allure.description("Тест проверяет успешное редактирование объявления владельцем")
    def test_edit_listing_by_owner(self, created_listing):
        with allure.step("Подготовить данные для обновления"):
            updated_payload = ListingGenerator.generate_listing_data(price='2000')
        
        with allure.step("Отправить запрос на редактирование объявления"):
            response = ApiClient.patch_request_update_listing(
                created_listing["owner_headers"],
                created_listing["listing_id"],
                updated_payload
            )
        
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, (
                AssertMessages.STATUS_CODE_MISMATCH.format(expected=200, actual=response.status_code)
                + f" Response: {response.text}"
            )
        with allure.step("Проверить, что цена объявления изменилась"):
            new_price = response.json()['price']
            assert created_listing["original_price"] != new_price, (
                f"Цена не изменилась: было {created_listing['original_price']}, стало {new_price}"
            )
            assert new_price == int(updated_payload['price']), (
                AssertMessages.FIELD_VALUE_MISMATCH.format(
                    field_name='price',
                    expected=int(updated_payload['price']),
                    actual=new_price
                )
            )
    
    @allure.epic("Listing API")
    @allure.feature("Редактирование объявления")
    @allure.title("Редактирование объявления: негативный кейс (без авторизации)")
    @allure.description("Тест проверяет ошибку при редактировании без токена")
    def test_edit_listing_unauthorized(self, created_listing):
        with allure.step("Подготовить данные для обновления"):
            updated_payload = ListingGenerator.generate_listing_data(price='2000')
            headers_unauthorized = {}
        
        with allure.step("Отправить запрос на редактирование без авторизации"):
            response = ApiClient.patch_request_update_listing(
                headers_unauthorized,
                created_listing["listing_id"],
                updated_payload
            )
        
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 401, (
                AssertMessages.STATUS_CODE_MISMATCH.format(expected=401, actual=response.status_code)
                + f" Response: {response.text}"
            )
        with allure.step("Проверить тело ответа"):
            response_data = response.json()
            # API возвращает поле 'messege' вместо 'message' (опечатка в API)
            assert response_data.get('messege') == ErrorResponseMessages.TOKEN_INVALID, (
                AssertMessages.FIELD_VALUE_MISMATCH.format(
                    field_name='messege',
                    expected=ErrorResponseMessages.TOKEN_INVALID,
                    actual=response_data.get('messege')
                )
            )
    
    @allure.epic("Listing API")
    @allure.feature("Редактирование объявления")
    @allure.title("Редактирование объявления: негативный кейс (чужое объявление)")
    @allure.description("Тест проверяет ошибку при редактировании чужого объявления")
    def test_edit_listing_by_another_user(self, created_listing, register_new_user):
        with allure.step("Подготовить данные для обновления"):
            _, another_headers = register_new_user
            updated_payload = ListingGenerator.generate_listing_data(price='2000')
        
        with allure.step("Отправить запрос на редактирование чужого объявления"):
            response = ApiClient.patch_request_update_listing(
                another_headers,
                created_listing["listing_id"],
                updated_payload
            )
        
        with allure.step("Проверить статус код ответа (401 Unauthorized)"):
            assert response.status_code == 401, (
                AssertMessages.STATUS_CODE_MISMATCH.format(expected=401, actual=response.status_code) +
                f" Response: {response.text}"
            )
        with allure.step("Проверить текст сообщения об ошибке"):
            assert response.json()['message'] == ErrorResponseMessages.LISTING_NOT_FOUND_OR_NO_PERMISSION, (
                AssertMessages.FIELD_VALUE_MISMATCH.format(
                    field_name='message',
                    expected=ErrorResponseMessages.LISTING_NOT_FOUND_OR_NO_PERMISSION, 
                    actual=response.json()['message']
                )
            )