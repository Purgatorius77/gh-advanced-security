from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, It's a sample app!"

@app.route('/api')
def get_api_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        data = response.json()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

import os

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
