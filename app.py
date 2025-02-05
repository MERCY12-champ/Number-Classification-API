from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Helper functions
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
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

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        return response.text if response.status_code == 200 else "No fun fact available."
    except Exception:
        return "No fun fact available."

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
    app.run(debug=True)