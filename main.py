from flask import Flask, jsonify
from datetime import datetime
import re

app = Flask(__name__)

# (A) Route with current date
@app.route('/<date_path>', methods=['GET'])
@app.route('/<date_path>/', methods=['GET'])
def date_route(date_path):
    try:
        datetime.strptime(date_path, '%d%m%y')

        today = datetime.now().strftime('%d-%m-%Y')
        response = jsonify({
            "date": today,
            "login": "sainpostman"  # Your login
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

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 