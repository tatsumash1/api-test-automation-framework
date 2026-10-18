# API test automation framework

Учебный проект для автоматизации тестирования REST API с помощью `pytest`, `requests` и `jsonschema`.

В проекте используется [ReqRes API](https://reqres.in/).

## Структура проекта

```text
.
├── clients/
│   └── reqres_client.py       # клиент для HTTP-запросов ReqRes
├── schemas/
│   ├── auth_schemas.py        # схемы ответов регистрации и логина
│   ├── products_schemas.py    # схемы ресурсов и продуктов
│   └── user_schemas.py        # схемы пользователей и обновления пользователя
├── tests/
│   ├── integration/           # тесты с реальными запросами к ReqRes
│   │   ├── test_auth.py
│   │   ├── test_products.py
│   │   └── test_users.py
│   └── unit/                  # тесты клиента без сети
│       └── test_reqres_client.py
├── conftest.py                # фикстуры base_url, api_session и reqres_client
├── pytest.ini                 # пути тестов и pytest-маркеры
└── requirements.txt
```

## Реализованные позитивные сценарии

### Пользователи

- [x] `GET /api/users/{user_id}` — получение пользователя, параметризованный тест и проверка JSON-схемы
- [x] `GET /api/users?page={page_id}` — получение списка пользователей, параметризованный тест и проверка схемы списка
- [x] `PUT /api/users/2` — полное обновление пользователя и проверка схемы ответа
- [x] `PATCH /api/users/2` — обновление только `name`
- [x] `PATCH /api/users/2` — обновление только `job`
- [x] `PATCH /api/users/2` — обновление `name` и `job`
- [x] `DELETE /api/users/2` — удаление пользователя
- [x] `POST /api/users` — создание пользователя и проверка JSON-схемы

### Ресурсы и продукты

- [x] `GET /api/unknown` — получение списка ресурсов и проверка схемы списка
- [x] `GET /api/products/{product_id}` — получение продукта, параметризованный тест и проверка JSON-схемы
- [x] `GET /api/products?page={page_id}` — получение страницы продуктов
- [x] Проверка пустых страниц продуктов через поле `total_pages`

### Авторизация

- [x] `POST /api/register` — успешная регистрация и проверка схемы ответа
- [x] `POST /api/login` — успешный логин и проверка схемы ответа

## Реализованные негативные сценарии

- [x] `GET /api/users/{user_id}` — несуществующие пользователи `0`, `2500`, `3000`
- [x] `GET /api/products/{product_id}` — несуществующие продукты `9999`, `10000`, `10001`
- [x] `POST /api/register` — параметризованные невалидные payload'ы
- [x] `POST /api/login` — параметризованные невалидные payload'ы
- [x] Проверка структуры ошибок через JSON-схему

## Фикстуры и клиент

`conftest.py` предоставляет общие фикстуры:

- `base_url` — базовый URL из переменной `BASE_URL` или значение по умолчанию `https://reqres.in/api`;
- `api_session` — общая `requests.Session`, закрываемая после завершения тестов;
- `reqres_client` — экземпляр `ReqresClient`, через который тесты выполняют API-запросы.

## JSON-схемы

Ответы проверяются с помощью библиотеки `jsonschema`.

- `schemas/user_schemas.py` — пользователь, список пользователей, PUT/PATCH-ответы;
- `schemas/products_schemas.py` — ресурс, продукт и список продуктов;
- `schemas/auth_schemas.py` — успешная регистрация, логин и ошибки авторизации.

Схема проверяет структуру и типы полей, а обычные `assert` — бизнес-условия, например соответствие `id` запрошенному пользователю.

## Unit- и integration-тесты

Integration-тесты в `tests/integration/` отправляют реальные запросы к ReqRes и проверяют поведение API.

Unit-тесты в `tests/unit/` не обращаются к сети. Они используют mock-сессию и проверяют, что `ReqresClient` правильно формирует HTTP-метод, URL, заголовки, timeout и JSON-payload.

## Маркеры pytest

В проекте зарегистрированы маркеры:

- `smoke` — основные быстрые проверки;
- `negative` — негативные сценарии;
- `auth` — регистрация и авторизация;
- `users` — тесты пользователей;
- `products` — тесты продуктов.
- `integration` — тесты с реальными запросами к ReqRes;
- `unit` — изолированные тесты без сетевых запросов.

Примеры запуска:

```powershell
# все тесты
pytest -v

# только smoke-тесты
pytest -m smoke -v

# только негативные тесты
pytest -m negative -v

# smoke-тесты пользователей
pytest -m "smoke and users" -v

# только интеграционные тесты
pytest -m integration -v

# только unit-тесты
pytest -m unit -v

# unit-тесты без обращения к API
pytest tests/unit -v
```

## Установка и запуск

Создание виртуального окружения и установка зависимостей:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Запуск всех тестов:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

### Переменные окружения

Базовый URL можно изменить через `BASE_URL`:

```powershell
$env:BASE_URL = "https://reqres.in/api"
```

Часть endpoint'ов `/api/products` требует API-ключа. Ключ не должен храниться в репозитории:

```powershell
$env:REQRES_API_KEY = "ваш-api-ключ"
.\.venv\Scripts\python.exe -m pytest -v
```

Без `REQRES_API_KEY` защищённые тесты продуктов будут отмечены как `skipped`, а остальные тесты продолжат выполняться.

Проверить наличие ключа можно так:

```powershell
if ($env:REQRES_API_KEY) {
    "API key установлен"
} else {
    "API key отсутствует"
}
```
