import allure
from helpers.api_client import ApiClient
from data.error_messages import AssertMessages
from data.response_messages import SuccessMessages


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
                + f" Response: {response.text}"
            )
        with allure.step("Проверить текст сообщения об успешном удалении"):
            assert response.json()['message'] == SuccessMessages.LISTING_DELETED, (
                AssertMessages.FIELD_VALUE_MISMATCH.format(
                    field_name='message',
                    expected=SuccessMessages.LISTING_DELETED,
                    actual=response.json()['message']
                )
            )