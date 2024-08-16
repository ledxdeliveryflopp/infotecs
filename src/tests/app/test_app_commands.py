import subprocess
from asyncio import sleep
import allure
import pytest


@pytest.mark.commands
@allure.feature('Тестирование функционала управления API')
class TestApiCommands:

    @classmethod
    @allure.title("Тестирование остановки API")
    @allure.description("Тестирование функционала управление API")
    @allure.tag("api commands")
    async def test_stop_api(cls) -> None:
        with allure.step("попытка остановки API"):
            command = subprocess.run(["webcalculator.exe", "stop"], capture_output=True, text=True)
            await sleep(4)
        with allure.step("Проверка состояния API"):
            command_result = command.stdout
            result = command_result.split('\n')
            assert "Веб-калькулятор остановлен" == result[1]

    @classmethod
    @allure.title("Тестирование запуска API")
    @allure.description("Тестирование функционала управление API")
    @allure.tag("api commands")
    async def test_start_api(cls) -> None:
        with allure.step("попытка запуска API"):
            command = subprocess.run(["webcalculator.exe", "start", "localhost", "5413"],
                                     capture_output=True, text=True)
            await sleep(4)
        with allure.step("Проверка состояния API"):
            command_result = command.stdout
            result = command_result.split('\n')
            assert "Веб-калькулятор запущен на localhost:5413" == result[1]

    @classmethod
    @allure.title("Тестирование перезапуска API")
    @allure.description("Тестирование функционала управление API")
    @allure.tag("api commands")
    async def test_restart_api(cls) -> None:
        with allure.step("попытка перезапуска API"):
            command = subprocess.run(["webcalculator.exe", "restart"],
                                     capture_output=True, text=True)
            await sleep(4)
        with allure.step("Проверка состояния API"):
            command_result = command.stdout
            result = command_result.split('\n')
            assert "Веб-калькулятор запущен на localhost:5413" == result[3]
