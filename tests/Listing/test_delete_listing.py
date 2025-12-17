import allure
from helpers.api_client import ApiClient
from config.error_messages import AssertMessages


class TestDeleteListing:
    
    @allure.epic("Listing API")
    @allure.feature("Удаление объявления")
    @allure.title("Удаление объявления: позитивный кейс")
    @allure.description("Тест проверяет успешное удаление объявления")
    def test_delete_listing(self, created_listing):
        with allure.step("Отправить запрос на удаление объявления"):
            response = ApiClient.delete_request_delete_listing(
                created_listing["owner_headers"], 
                created_listing["listing_id"]
            )
        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, (
                AssertMessages.STATUS_CODE_MISMATCH.format(expected=200, actual=response.status_code)
            )
        with allure.step("Проверить текст сообщения об успешном удалении"):
            expected_message = "Объявление удалено успешно"
            assert response.json()['message'] == expected_message, (
                AssertMessages.ERROR_MESSAGE_MISMATCH.format(expected=expected_message, actual=response.json()['message'])
            )