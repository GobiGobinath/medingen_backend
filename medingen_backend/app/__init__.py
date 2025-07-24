from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL

mysql = MySQL()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)
    mysql.init_app(app)
    jwt.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp
    from .routes.review_routes import review_bp
    from .routes.salt_routes import salt_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(salt_bp)

    return app
