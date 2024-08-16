# infotecs
 Тестовое задание на автотестирование Python в ИнфоТеКС

# Первоначальная установка

1. Установим менеджер пакетов Poetry.
```bash 
pip install poetry
```
2. Установим необходимые библиотеки.
```bash 
poetry install
```

# Запуск тестов

1. Запустим все тесты
```bash 
pytest
```

# Запуск определенных тестов

1. Доступные тесты
```bash 
    commands: Тестирование управлением приложением,
    addition: Тестирование эндпоинтов сложения,
    division: Тестирование эндпоинтов деления,
    multiplication: Тестирование эндпоинтов умножения,
    remainder: Тестирование эндпоинтов деления с остатком,
    state: Тестирование эндпоинта состояния сервера
```
2. Пример
```bash 
pytest -v -m commands
```

# Запуск тестов c логирование Pytest

1. Запуск тестов с логированием в log файл
```bash 
pytest > test_result.log
```

# тесты c логированием Allure(windows)

1. Установим Scoop
```bash 
scoop install allure
```
2. Проверим версию Allure
```bash 
allure --version
```

# Запуск тестов с логированием Allure
1. Запустим тесты
```bash 
pytest
```
2. Запустим Allure
```bash 
allure serve allure-results
```

3.Пример отчета

![plot](/static/allure.png)