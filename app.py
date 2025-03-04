from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models import db # Import db from models/__init__.py

# app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)

    # Initial Extensions
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    # Import models to ensure they are registered with SQLAlchemy
    from models.user import User
    from models.campaign import Campaign

    # Register Blueprints
    from routes.user_routes import user_bp
    from routes.campaign_routes import campaign_bp
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(campaign_bp, url_prefix="/campaigns")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
