from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db # Import db from models/__init__.py

app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load config
    app.config.from_object('config.Config')

    # Initial Extensions
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    # Import models to ensure they are registered with SQLAlchemy
    from models.user import User

    # Register Blueprints
    from routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
