from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

import config

# Globally accessible libraries
db:SQLAlchemy = SQLAlchemy()
migrate:Migrate = Migrate()
ma:Marshmallow = Marshmallow()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.DevelopmentConfig)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    with app.app_context():

        # Include our Routes
        from .routes.views import views
        from .routes.videos import videos
        from .routes.personRoute import personRoute


        # Import Models
        #from .models.person import Person, PersonResource
        from .models.video import Video
        from .models.person import Person
        
        # Register Blueprints
        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(videos, url_prefix='/')
        app.register_blueprint(personRoute, url_prefix='/')

        db.create_all()

        return app