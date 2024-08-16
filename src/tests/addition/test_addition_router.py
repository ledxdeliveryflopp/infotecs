import allure


@allure.feature('Тестирование сложения')
class TestAdditionRouter:
    """Тестирование эндпоинта сложения чисел"""
    url: str = "addition"
    success_json: dict = {"x": 42, "y": 24}
    failed_json_format: dict = {"x": "avbs", "y": 24}
    failed_json_keys: dict = {"y": 24}
    failed_json_long_int: dict = {"x": 23123124124124124, "y": 123124213}

    @classmethod
    @allure.title("Тестирование сложения API(успешное сложение)")
    @allure.description("Тестирование успешного сложения 2х чисел")
    @allure.tag("addition")
    async def test_success_addiction(cls, HttpxClient) -> None:
        """Тестирование успешного сложения"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.success_json)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {"statusCode": 0, "result": 66}

    @classmethod
    @allure.title("Тестирование валидации сложения API(не верный формат тела запроса)")
    @allure.description("Тестирование валидации при сложении если передать json с неверными ключами")
    @allure.tag("addition")
    async def test_addiction_bad_json_keys(cls, HttpxClient) -> None:
        """Тестирование валидации сложения при передаче не верных ключей в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.failed_json_keys)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {'statusCode': 2, 'statusMessage': 'Не указаны необходимые параметры'}

    @classmethod
    @allure.title("Тестирование валидации сложения API(Одно из значений не является целым числом)")
    @allure.description("Тестирование валидации при сложении если передать в body не верные типы данных ")
    @allure.tag("addition")
    async def test_addiction_bad_types(cls, HttpxClient) -> None:
        """Тестирование валидации сложения при передаче не верного формата данных в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.failed_json_format)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}

    @classmethod
    @allure.title("Тестирование валидации сложения API(Превышен размер одного из значений)")
    @allure.description("Тестирование валидации при сложении если передать в body большое число ")
    @allure.tag("addition")
    async def test_addiction_long_int(cls, HttpxClient) -> None:
        """Тестирование валидации сложения при передаче больших чисел в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=cls.failed_json_long_int)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}

    @classmethod
    @allure.title("Тестирование ошибки сложения API(Неправильный формат тела запроса)")
    @allure.description("Тестирование валидации при сложении если не передать body")
    @allure.tag("addition")
    async def test_addiction_empty_body(cls, HttpxClient) -> None:
        """Тестирование валидации сложения при пустом body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {'statusCode': 5, 'statusMessage': 'Не допустимый формат json'}
