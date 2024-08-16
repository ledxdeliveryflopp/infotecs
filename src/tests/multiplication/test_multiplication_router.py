import allure
import pytest
from src.settings.const import Const


@pytest.mark.multiplication
@allure.feature('Тестирование умножения')
class TestMultiplicationRouter:
    url: str = "multiplication"

    @classmethod
    @allure.title("Тестирование умножения API(успешное умножение)")
    @allure.description("Тестирование успешного умножения 2х чисел")
    @allure.tag("multiplication")
    async def test_success_multiplication(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.SUCCESS_JSON)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {"statusCode": 0, "result": 20}

    @classmethod
    @allure.title("Тестирование валидации умножения API(не верный формат запроса)")
    @allure.description("Тестирование валидации при умножении если передать json с неверными ключами")
    @allure.tag("multiplication")
    async def test_multiplication_bad_json_keys(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_KEYS)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS

    @classmethod
    @allure.title("Тестирование валидации умножения API(Одно из значений не является целым числом)")
    @allure.description("Тестирование валидации при умножении если передать в body не верные типы "
                        "данных ")
    @allure.tag("multiplication")
    async def test_multiplication_bad_types(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_FORMAT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS_FORMAT

    @classmethod
    @allure.title("Тестирование валидации умножения API(Превышен размер одного из значений)")
    @allure.description("Тестирование валидации при умножении если передать в body большое число ")
    @allure.tag("multiplication")
    async def test_multiplication_long_int(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_LONG_INT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.LONG_INT

    @classmethod
    @allure.title("Тестирование ошибки умножения API(Неправильный формат тела запроса)")
    @allure.description("Тестирование валидации при умножении если не передать body")
    @allure.tag("multiplication")
    async def test_multiplication_empty_body(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_JSON_FORMAT

