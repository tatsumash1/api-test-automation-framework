# Репозиторий проект для демонстрации навыков в тестировании API с помощью pytest

Для работы был выбрал ReqRes API

## Реализованые позитивные методы:

### GET методы

- [x] GET /api/users/{user_id} - тест на получение пользователя по id (метод параметризован)
- [x] GET /api/unknown
- [x] GET /api/user?page={page_id} - тест на получение списка пользователей (метод параметризирован)
- [x] GET /api/products/{product_id} - тест на получение товара по id (метод параметризован)
- [x] GET /api/products?page={p_page_id} - тест на получение списка продуктов (метод параметризован)

### POST методы

- [x] POST /api/register - тест на регистрацию пользователя
- [x] POST /api/login - тест на успешный логин

### PUT методы

- [x] PUT /api/users/2 - тест на полное изменение пользователя

### PATCH методы

- [x] PATCH /api/users/2 (тест на обновление только name)
- [x] PATCH /api/users/2 (тест на обновление только job)
- [x] PATCH /api/users/2 (тест на обновление name и job)

### DELETE методы

- [x] DELETE /api/users/2

## Реализованые негативные методы:

### GET методы

- [x] GET /api/users/2500

### POST методы

- [x] POST /api/register (тест на регистрацию без пароля)
- [x] POST /api/login (тест на вход без пароля)

## Запуск тестов

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Часть актуальных эндпоинтов ReqRes требует API-ключ. Ключ не должен храниться
в репозитории: перед запуском передайте его через переменную окружения.

```powershell
$env:REQRES_API_KEY = "ваш-api-ключ"
.\.venv\Scripts\python.exe -m pytest -v
```

Без `REQRES_API_KEY` защищённые тесты `/api/products` будут отмечены как
пропущенные (`skipped`), а остальные тесты продолжат выполняться.

Проверка установки апи-ключа:

```powershell
if ($env:REQRES_API_KEY) { "API key установлен" } else { "API key отсутствует" }
```
