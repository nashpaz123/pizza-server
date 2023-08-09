from flask import Flask, request, jsonify

app = Flask(__name__)

# some dummy database to store orders
orders = []

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json

    pizza_type = data.get('pizza-type')
    size = data.get('size')
    amount = data.get('amount')

    if not pizza_type or not size or not amount:
        return jsonify({"error": "Missing required fields"}), 400

    order = {
        "pizza-type": pizza_type,
        "size": size,
        "amount": amount
    }

    orders.append(order)

    return jsonify({"message": "Order placed successfully"}), 201

@app.route('/health', methods=['GET'])
def check_health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)