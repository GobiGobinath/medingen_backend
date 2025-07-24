from flask import Blueprint, jsonify
from app import mysql

review_bp = Blueprint('review', __name__, url_prefix='/api/reviews')

@review_bp.route('/', methods=['GET'])
def get_reviews():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()
    cursor.close()
    reviews = [{'id': row[0], 'product_id': row[1], 'username': row[2], 'rating': row[3], 'comment': row[4]} for row in data]
    return jsonify(reviews)
