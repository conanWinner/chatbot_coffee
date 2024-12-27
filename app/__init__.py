from flask import Flask
from .service.mongodb_service import get_mongo_client
from .routes import bp as main_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Kết nối MongoDB
    mongo_uri = app.config["MONGO_URI"]
    app.mongo_client = get_mongo_client(mongo_uri)

    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Đăng ký Blueprint
    app.register_blueprint(main_bp)

    return app
