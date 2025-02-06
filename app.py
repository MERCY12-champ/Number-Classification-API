from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import functools
import time

app = Flask(__name__)
CORS(app)

# Cache decorator
def cache(timeout=60):
    def decorator(func):
        cached_results = {}
        last_updated = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.items())
            current_time = time.time()

            if key in cached_results and (current_time - last_updated[key]) < timeout:
                return cached_results[key]

            result = func(*args, **kwargs)
            cached_results[key] = result
            last_updated[key] = current_time
            return result

        return wrapper
    return decorator

# Helper functions
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    digits = list(map(int, str(abs(n))))
    power = len(digits)
    return sum(digit**power for digit in digits) == abs(n)

@cache(timeout=300)  # Cache results for 5 minutes
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
        return response.text if response.status_code == 200 else "No fun fact available."
    except requests.Timeout:
        return "No fun fact available due to timeout."
    except Exception:
        return "No fun fact available."

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Number Classification API!",
        "usage": "Use /api/classify-number?number=<integer> to classify a number."
    }), 200

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []

    # Classify the number
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    digit_sum = sum(int(digit) for digit in str(abs(number)))

    # Prepare the response
    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": get_fun_fact(number)
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    # Bind to 0.0.0.0 to accept connections from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)