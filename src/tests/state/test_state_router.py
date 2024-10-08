import allure
import pytest


@pytest.mark.state
@allure.feature('Тестирование статуса API')
class TestStateRouter:
    url: str = "state"

    @classmethod
    @allure.title("Тестирование состяния API")
    @allure.description("Тестирование 200 статус кода от API")
    @allure.tag("State")
    async def test_state_ok(cls, HttpxClient):
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.get(url=cls.url)
        with allure.step("Сравнение ожидаемого статус кода"):
            assert response.json() == {'statusCode': 0, 'state': 'OК'}
