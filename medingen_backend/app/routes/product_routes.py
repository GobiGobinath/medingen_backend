from flask import Blueprint, jsonify
from app import mysql

product_bp = Blueprint('product', __name__, url_prefix='/api/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    cursor.close()
    products = [{'id': row[0], 'name': row[1], 'image_url': row[2]} for row in data]
    return jsonify(products)
