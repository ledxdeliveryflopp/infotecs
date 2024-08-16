import allure
import pytest
from src.settings.const import Const


@pytest.mark.addition
@allure.feature('Тестирование сложения')
class TestAdditionRouter:
    url: str = "addition"

    @classmethod
    @allure.title("Тестирование сложения API(успешное сложение)")
    @allure.description("Тестирование успешного сложения 2х чисел")
    @allure.tag("addition")
    async def test_success_addiction(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.SUCCESS_JSON)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {"statusCode": 0, "result": 12}

    @classmethod
    @allure.title("Тестирование валидации сложения API(не верный формат тела запроса)")
    @allure.description("Тестирование валидации при сложении если передать json с неверными ключами")
    @allure.tag("addition")
    async def test_addiction_bad_json_keys(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_KEYS)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS

    @classmethod
    @allure.title("Тестирование валидации сложения API(Одно из значений не является целым числом)")
    @allure.description("Тестирование валидации при сложении если передать в body не верные типы данных ")
    @allure.tag("addition")
    async def test_addiction_bad_types(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_FORMAT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS_FORMAT

    @classmethod
    @allure.title("Тестирование валидации сложения API(Превышен размер одного из значений)")
    @allure.description("Тестирование валидации при сложении если передать в body большое число ")
    @allure.tag("addition")
    async def test_addiction_long_int(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_LONG_INT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.LONG_INT

    @classmethod
    @allure.title("Тестирование ошибки сложения API(Неправильный формат тела запроса)")
    @allure.description("Тестирование валидации при сложении если не передать body")
    @allure.tag("addition")
    async def test_addiction_empty_body(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_JSON_FORMAT
