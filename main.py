from flask import Flask, jsonify, Response, request
from datetime import datetime
import re
import requests

app = Flask(__name__)

MOODLE_LOGIN = "sainpostman"  # Ваш логин

# Корневой маршрут для нового задания
@app.route('/', methods=['GET'])
def root():
    response = Response(MOODLE_LOGIN, mimetype='text/plain')
    response.headers['X-Author'] = MOODLE_LOGIN
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Задание 4 - маршрут /result4/
@app.route('/result4/', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def result4():
    # Получаем заголовок x-test из запроса
    x_test_value = request.headers.get('x-test', '')
    
    # Получаем тело запроса
    try:
        body_content = request.get_data(as_text=True)
    except:
        body_content = ''
    
    # Создаем JSON ответ
    result = {
        "message": MOODLE_LOGIN,
        "x-result": x_test_value,
        "x-body": body_content
    }
    
    response = jsonify(result)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'x-test,ngrok-skip-browser-warning,Content-Type,Accept,Access-Control-Allow-Headers'
    
    return response

# Новое задание - маршрут /login/
@app.route('/login/', methods=['GET'])
def login_with_charset():
    response = Response(MOODLE_LOGIN, mimetype='text/plain; charset=UTF-8')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Новое задание - маршрут /promise/
@app.route('/promise/', methods=['GET'])
def promise_function():
    js_code = """function task(x) {
    return new Promise((resolve, reject) => {
        if (x < 18) {
            resolve('yes');
        } else {
            reject('no');
        }
    });
}"""
    response = Response(js_code, mimetype='text/plain')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Новое задание - маршрут /fetch/
@app.route('/fetch/', methods=['GET'])
def fetch_page():
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Fetch Page</title>
</head>
<body>
    <input type="text" id="inp">
    <button id="bt">Fetch</button>
    
    <script>
        document.getElementById('bt').addEventListener('click', function() {
            const url = document.getElementById('inp').value;
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('inp').value = data;
                })
                .catch(error => {
                    document.getElementById('inp').value = 'Error: ' + error;
                });
        });
    </script>
</body>
</html>'''
    response = Response(html_content, mimetype='text/html; charset=UTF-8')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Новое задание - маршрут /sample/
@app.route('/sample/', methods=['GET'])
def sample_function():
    js_code = """function task(x) {
    return x * this * this;
}"""
    response = Response(js_code, mimetype='text/plain')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# (A) Route with current date
@app.route('/<date_path>', methods=['GET'])
@app.route('/<date_path>/', methods=['GET'])
def date_route(date_path):
    try:
        datetime.strptime(date_path, '%d%m%y')

        today = datetime.now().strftime('%d-%m-%Y')
        response = jsonify({
            "date": today,
            "login": MOODLE_LOGIN
        })
        response.headers['Content-Type'] = 'application/json'
        return response

    except ValueError:
        return "Invalid date format", 400

# (B) Route for string reversal
@app.route('/api/rv/<string:input_str>', methods=['GET'])
@app.route('/api/rv/<string:input_str>/', methods=['GET'])
def reverse_string(input_str):
    if not re.fullmatch(r'[a-z]+', input_str):
        return "Invalid input string", 400

    return input_str[::-1]

@app.route('/login', methods=['GET'])
def get_login():
    return Response(MOODLE_LOGIN, mimetype='text/plain')

@app.route('/id/<int:N>', methods=['GET'])
@app.route('/id/<int:N>/', methods=['GET'])
def get_user_login(N):
    try:
        # Запрос БЕЗ заголовка Content-Type
        response = requests.get(f'https://nd.kodaktor.ru/users/{N}')
        response.raise_for_status()

        user_data = response.json()
        login = user_data.get('login', '')
        return Response(login, mimetype='text/plain')

    except requests.RequestException:
        return Response("Error fetching data", status=500, mimetype='text/plain')
    except Exception:
        return Response("Error processing request", status=500, mimetype='text/plain')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'x-test,ngrok-skip-browser-warning,Content-Type,Accept,Access-Control-Allow-Headers'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 