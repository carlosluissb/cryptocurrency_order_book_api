from flask import Flask

def create_app():
    """
    Create and configure an instance of the Flask application.

    Returns:
        Flask: The Flask application.
    """
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp)

    return app
