from flask import Blueprint

app_api = Blueprint('api', __name__)

from app.rest import hello_world
from app.rest import add
from app.rest import all
