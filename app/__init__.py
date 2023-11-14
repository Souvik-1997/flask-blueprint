from flask import Flask
import pymongo
import os
from config import Config


try:
    client = pymongo.MongoClient(Config.MONGO_URI)
    client.server_info()
    db = client.logistics
    print(" * DB connection established...")

except pymongo.errors.ServerSelectionTimeoutError as err:
    print(" * Failed to connect DB", err)


flask_env = os.getenv("FLASK_ENV", None)
print(" * FLASK_ENV:", flask_env)

def create_app():
    app = Flask(__name__)

    if flask_env == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    # Import and register routes
    from app.routes import bp as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
