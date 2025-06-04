# Flask Web Application

Простое Flask приложение для выполнения задания 0047.

## Функциональность

### A) Маршрут с датой
`/<DDMMYY>/` - возвращает JSON с текущей датой и логином
- Пример: `/040625/` 
- Ответ: `{"date": "04-06-2025", "login": "sainpostman"}`

### B) Маршрут для переворота строки  
`/api/rv/<string>/` - возвращает перевернутую строку
- Пример: `/api/rv/abc/` 
- Ответ: `cba`

## Деплой на Render

1. Создайте репозиторий на GitHub и загрузите файлы:
   - `main.py` - основной файл приложения
   - `requirements.txt` - зависимости
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