# Репозиторий проект для демонстрации навыков в тестировании API с помощью pytest

Для работы был выбрал ReqRes API

## Реализованые методы:

### GET методы

- [x] GET /api/users/2
- [x] GET /api/users?page=2
- [x] GET /api/unknown
- [x] GET /api/products?page=1

### POST методы

- [x] POST /api/register
- [x] POST /api/login

### PUT методы

- [x] PUT /api/users/2

### PATCH методы

- [x] PATCH /api/users/2 (тест на обновление только name)
- [x] PATCH /api/users/2 (тест на обновление только job)
- [x] PATCH /api/users/2 (тест на обновление name и job)

### DELETE методы

- [x] DELETE /api/users/2

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
