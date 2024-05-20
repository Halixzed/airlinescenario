from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
    app.config.from_object('backend.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from backend.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return send_from_directory('../frontend/templates', 'index.html')

    return app

