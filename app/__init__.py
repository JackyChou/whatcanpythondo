# coding: utf-8

import os

from flask import Flask, request, g

from config import config
from app.extensions import bootstrap

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    # register blueprint
    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
