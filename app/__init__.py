from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Import your configuration

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration
    
    db.init_app(app)
    
    # Additional setup like blueprints, routes, etc...
    
    return app
