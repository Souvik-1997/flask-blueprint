import os

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", False)
    SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY")
    MONGO_URI = os.getenv("MONGO_URI", "MONGO_URI")



class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = os.getenv("FLASK_ENV", None)


class ProductionConfig(Config):
    pass