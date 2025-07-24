from flask import Blueprint, jsonify
from app import mysql

salt_bp = Blueprint('salt', __name__, url_prefix='/api/salts')

@salt_bp.route('/', methods=['GET'])
def get_salts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM salt_contents")
    data = cursor.fetchall()
    cursor.close()
    salts = [{'id': row[0], 'product_id': row[1], 'salt_name': row[2], 'quantity_mg': row[3]} for row in data]
    return jsonify(salts)
