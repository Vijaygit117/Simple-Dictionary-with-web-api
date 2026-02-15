from flask import Flask
from apis.dictionary_bp import dict_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(dict_bp)

    return app
