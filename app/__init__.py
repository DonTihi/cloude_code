from flask import Flask

from .routes import bp


def create_app(config: dict | None = None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    if config:
        app.config.update(config)

    app.register_blueprint(bp)

    return app
