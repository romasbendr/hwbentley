from flask import Flask


def create_app(config):
    """Core application"""
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object('config.Config')
        # separation for dev, test, prod envs
        # app.config.from_object('config.ProductionConfig')
        

    # initialise plugins such as dbs here

    with app.app_context():
        # chose bp as it is easier than simple routes in app factory setting
        from .routes import route_blueprint
        app.register_blueprint(route_blueprint)
        return app