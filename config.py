import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'your_jwt_secret_key'
    INITIAL_TOKEN_AMOUNT = 1000
    SPECIAL_TAG_COLLABORATIONS = 5
