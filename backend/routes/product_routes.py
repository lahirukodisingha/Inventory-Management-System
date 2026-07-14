from flask import Blueprint, request, jsonify
from controllers.product_controller import create_product, get_all_products

# Flask Blueprint එකක් සාදා ගැනීම (Routes ටික වෙන් කරලා තියාගන්න)
product_blueprint = Blueprint('product_routes', __name__)

# භාණ්ඩයක් ඇතුලත් කිරීමට ඇති Endpoint එක (POST Request)
@product_blueprint.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json() # පිටතින් එන JSON දත්ත ලබාගැනීම
    response, status_code = create_product(data)
    return jsonify(response), status_code

# සියලුම භාණ්ඩ ලබාගැනීමට ඇති Endpoint එක (GET Request)
@product_blueprint.route('/api/products', methods=['GET'])
def list_products():
    response, status_code = get_all_products()
    return jsonify(response), status_code