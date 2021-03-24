from flask import Blueprint

app_api = Blueprint('api', __name__)

from app.rest import hello_world
