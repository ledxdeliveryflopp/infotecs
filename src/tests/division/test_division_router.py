import allure
from src.settings.const import Const


@allure.feature('Тестирование деления')
class TestDivisionRouter:
    """Тестирование роутера деления чисел"""
    url: str = "division"

    @classmethod
    @allure.title("Тестирование деления API(успешное деление)")
    @allure.description("Тестирование успешного деления 2х чисел")
    @allure.tag("division")
    async def test_success_division(cls, HttpxClient) -> None:
        """Тестирование успешного деления"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.SUCCESS_JSON)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {"statusCode": 0, "result": 5}

    @classmethod
    @allure.title("Тестирование валидации деления API(не верный формат запроса)")
    @allure.description("Тестирование валидации при делении если передать json с неверными ключами")
    @allure.tag("division")
    async def test_division_bad_json_keys(cls, HttpxClient) -> None:
        """Тестирование валидации деления при передаче не верных ключей в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_KEYS)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS

    @classmethod
    @allure.title("Тестирование валидации деления API(Одно из значений не является целым числом)")
    @allure.description("Тестирование валидации при делении если передать в body не верные типы данных ")
    @allure.tag("division")
    async def test_division_bad_types(cls, HttpxClient) -> None:
        """Тестирование валидации деления при передаче не верного формата данных в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_FORMAT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS_FORMAT

    @classmethod
    @allure.title("Тестирование валидации деления API(Превышен размер одного из значений)")
    @allure.description("Тестирование валидации при делении если передать в body большое число ")
    @allure.tag("division")
    async def test_division_long_int(cls, HttpxClient) -> None:
        """Тестирование валидации деления при передаче больших чисел в body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_LONG_INT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.LONG_INT
    @classmethod
    @allure.title("Тестирование ошибки деления API(Неправильный формат тела запроса)")
    @allure.description("Тестирование валидации при делении если не передать body")
    @allure.tag("division")
    async def test_division_empty_body(cls, HttpxClient) -> None:
        """Тестирование валидации деления при пустом body"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_JSON_FORMAT

    @classmethod
    @allure.title("Тестирование ошибки деления API(Ошибка вычесления)")
    @allure.description("Тестирование валидации при делении на 0")
    @allure.tag("division")
    async def test_zero_division(cls, HttpxClient) -> None:
        """Тестирование валидации при делении на 0"""
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_ZERO_DIVISION)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.CALCULATION_ERROR
