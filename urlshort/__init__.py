from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app