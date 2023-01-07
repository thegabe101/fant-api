from flask import Flask
from flask_cors import CORS
import logging
import os
import sys

from api.views import mount_blueprints

def create_app():
    app = Flask(__name__)
    enviornment = 'dev'
    CORS(
        app,
        supports_credentials=True,
        origins=["localhost:3000"]
    )
    mount_blueprints(app)
    return app
