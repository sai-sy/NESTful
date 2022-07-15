import os
from dotenv import load_dotenv

class Config(object):
    # UX SPECFIC
    MAX_ACCOUNTS_UNDER_EMAIL = 4

    #load_dotenv()
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECRET_KEY = os.environ.get("SECRET_KEY")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG=True
    TESTING = True
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class SetupConfig(DevelopmentConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

