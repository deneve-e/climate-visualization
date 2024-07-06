from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from .models import ClimateData # Import here to avoid circular import
        db.create_all()

        from .routes import main
        app.register_blueprint(main)

    return app