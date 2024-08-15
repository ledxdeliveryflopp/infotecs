import allure


@allure.feature('Тестирование сложения')
class TestAdditionRouter:
    """Тестирование эндпоинта сложения чисел"""
    url: str = "addition"
    success_json: dict = {"x": 42, "y": 24}
    failed_json_format: dict = {"x": "avbs", "y": 24}

    @classmethod
    @allure.title("Тестирование сложения API")
    @allure.description("Тестирование успешного сложения 2х чисел")
    @allure.tag("addition")
    async def test_success_addiction(cls, HttpxClient) -> None:
        """Тестирование успешного сложения"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.success_json)
        with allure.step("Сравнение ожидаемого статус кода и ответа"):
            assert response.status_code == 200
            assert response.json() == {"statusCode": 0, "result": 66}

    @classmethod
    @allure.title("Тестирование ошибки сложения API")
    @allure.description("Тестирование ошибки при сложении")
    @allure.tag("addition")
    async def test_failed_addiction(cls, HttpxClient) -> None:
        """Тестирование ошибки при сложении"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.failed_json_format)
        with allure.step("Сравнение ожидаемого статус кода и ответа"):
            assert response.status_code == 200
            assert response.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
