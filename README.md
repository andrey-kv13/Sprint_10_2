# API Тесты QA Desk

Автоматизированные API тесты для платформы QA Desk на Python с использованием pytest и Allure.

## Структура проекта

```
├── config/
│   └── config.py           # Конфигурация API эндпоинтов
├── data/
│   ├── error_messages.py    # Шаблоны сообщений для assert
│   └── response_messages.py # Ожидаемые сообщения в ответах API
├── helpers/
│   ├── api_client.py       # Методы HTTP запросов
│   ├── common_generator.py # Генератор случайных строк
│   ├── listing_generator.py # Генератор тестовых данных объявлений
│   └── user_generator.py   # Генератор тестовых данных пользователей
├── tests/
│   ├── listing/
│   │   ├── test_create_create_listing.py
│   │   ├── test_delete_listing.py
│   │   └── test_edit_listing.py
│   └── user/
│       ├── test_user_login.py
│       └── test_user_registration.py
├── allure-report/          # HTML отчёт Allure
├── conftest.py             # Фикстуры pytest
├── pytest.ini              # Конфигурация pytest
└── requirements.txt        # Зависимости Python
```

## Покрытие тестами

| Функциональность | Тесты |
|------------------|-------|
| Регистрация пользователя | Успешная регистрация, Повторная регистрация (дубликат email) |
| Авторизация пользователя | Успешная авторизация |
| Создание объявления | Успешное создание |
| Редактирование объявления | Редактирование владельцем, Без авторизации, Чужое объявление |
| Удаление объявления | Успешное удаление |

## Установка

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
# Запуск всех тестов
pytest

# Запуск с генерацией данных для Allure
pytest --alluredir=allure-results

# Генерация HTML отчёта
allure generate allure-results --clean -o allure-report

# Открыть отчёт
allure open allure-report
```

## Технологии

- Python 3.10
- pytest 7.4.3
- requests 2.31.0
- requests-toolbelt 1.0.0
- allure-pytest 2.13.2
