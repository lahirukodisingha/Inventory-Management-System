from flask import Flask, jsonify
from flask_cors import CORS
from routes.product_routes import product_blueprint # අලුතින් හදපු route එක import කිරීම

app = Flask(__name__)
CORS(app)

# Product Routes ටික Flask app එකට ලියාපදිංචි (Register) කිරීම
app.register_blueprint(product_blueprint)

# සර්වර් එක වැඩදැයි බැලීමට ඇති මූලික පිටුව
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Inventory Management System Backend is Running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)