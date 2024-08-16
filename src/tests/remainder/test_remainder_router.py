import allure
from src.settings.const import Const


@allure.feature('Тестирование остатка от деления')
class TestRemainderRouter:
    """Тестирование роутера деления чисел c остатком"""
    url: str = "remainder"

    @classmethod
    @allure.title("Тестирование деления с остатком API(успешное деление)")
    @allure.description("Тестирование успешного деления с остатком 2х чисел")
    @allure.tag("remainder")
    async def test_success_remainder(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url,
                                              json=Const.json_const.SUCCESS_REMAINDER_JSON)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == {"statusCode": 0, "result": 1}

    @classmethod
    @allure.title("Тестирование валидации деления с остатком API(не верный формат запроса)")
    @allure.description("Тестирование валидации при делении  с остатком если передать json с неверными "
                        "ключами")
    @allure.tag("remainder")
    async def test_remainder_bad_json_keys(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_KEYS)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS

    @classmethod
    @allure.title("Тестирование валидации деления с остатком API(Одно из значений не является целым числом)")
    @allure.description("Тестирование валидации при делении с остатком если передать в body не верные типы "
                        "данных ")
    @allure.tag("remainder")
    async def test_remainder_bad_types(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_FORMAT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_KEYS_FORMAT

    @classmethod
    @allure.title("Тестирование валидации деления с остатком API(Превышен размер одного из значений)")
    @allure.description("Тестирование валидации при делении с остатком если передать в body большое число ")
    @allure.tag("remainder")
    async def test_remainder_long_int(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_LONG_INT)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.LONG_INT

    @classmethod
    @allure.title("Тестирование ошибки деления API(Неправильный формат тела запроса)")
    @allure.description("Тестирование валидации при делении если не передать body")
    @allure.tag("remainder")
    async def test_remainder_empty_body(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.BAD_JSON_FORMAT

    @classmethod
    @allure.title("Тестирование ошибки деления API(Ошибка вычесления)")
    @allure.description("Тестирование валидации при делении на 0")
    @allure.tag("remainder")
    async def test_remainder_zero_division(cls, HttpxClient) -> None:
        with allure.step(f'Отправка запроса на эндпоинт - {cls.url}'):
            response = await HttpxClient.post(url=cls.url, json=Const.json_const.FAILED_JSON_ZERO_DIVISION)
        with allure.step("Сравнение ожидаемого ответа"):
            assert response.json() == Const.json_error_const.CALCULATION_ERROR
