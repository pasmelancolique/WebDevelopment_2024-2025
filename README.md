# Flask Web Application

Простое Flask приложение для выполнения нескольких заданий.

## Функциональность

### Корневой маршрут
`/` - возвращает логин с кастомными заголовками
- Пример: `/`
- Ответ: `sainpostman`
- Заголовки: `X-Author: sainpostman`, `Access-Control-Allow-Origin: *`

### Задание 4 (CORS + JSON)

#### Маршрут /result4/
`/result4/` - возвращает JSON с данными из заголовков и тела запроса
- Методы: GET, POST, PUT, DELETE, OPTIONS
- Ответ: `{"message": "sainpostman", "x-result": "значение_x-test", "x-body": "тело_запроса"}`
- Полная поддержка CORS с кастомными заголовками

### Новейшее задание (неделя 3)

#### A) Маршрут /login/
`/login/` - возвращает логин 
- Пример: `/login/`
- Ответ: `sainpostman`
- Заголовки: `Access-Control-Allow-Origin: *`

#### B) Маршрут /promise/
`/promise/` - возвращает JavaScript код функции task с промисом
- Пример: `/promise/`
- Ответ: функция, которая возвращает промис (resolve 'yes' если x < 18, reject 'no' иначе)

#### C) Маршрут /fetch/
`/fetch/` - HTML страница с fetch функциональностью
- Пример: `/fetch/`
- Ответ: HTML страница с input (id="inp") и button (id="bt")
- При клике на кнопку делается fetch запрос к URL из поля ввода

### Предыдущие задания

#### Маршрут /sample/
`/sample/` - возвращает JavaScript код функции task
- Пример: `/sample/`
- Ответ: JavaScript функция, которая возвращает x * this * this

### Задание 0047

#### A) Маршрут с датой
`/<DDMMYY>/` - возвращает JSON с текущей датой и логином
- Пример: `/040625/` 
- Ответ: `{"date": "04-06-2025", "login": "sainpostman"}`

#### B) Маршрут для переворота строки  
`/api/rv/<string>/` - возвращает перевернутую строку
- Пример: `/api/rv/abc/` 
- Ответ: `cba`

### Второе задание

#### A) Маршрут с логином
`/login` - возвращает логин в системе MOODLE
- Пример: `/login`
- Ответ: `sainpostman`

#### B) Маршрут для получения логина пользователя по ID
`/id/<N>` - делает запрос к внешнему API и возвращает логин пользователя
- Пример: `/id/123`
- Ответ: логин пользователя с ID 123 из https://nd.kodaktor.ru/users/123

## Деплой на Render

1. Создайте репозиторий на GitHub и загрузите файлы:
   - `main.py` - основной файл приложения
   - `requirements.txt` - зависимости (Flask, Werkzeug, gunicorn, requests)
   - `runtime.txt` - версия Python
   - `Procfile` - команда запуска
   
2. На Render.com:
   - New Web Service
   - Подключите GitHub репозиторий
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`

## Локальный запуск

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Приложение будет доступно на `http://localhost:8080` 