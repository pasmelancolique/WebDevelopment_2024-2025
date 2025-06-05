from flask import Flask, jsonify, Response
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
@app.route('/login/', methods=['GET'])
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
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 