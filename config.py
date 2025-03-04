import os

class Config:
    # Configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin123:admin123@localhost/crow_funding_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'supersecretkey')