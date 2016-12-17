from flask import Blueprint
from .models import *

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    return 'Test'
