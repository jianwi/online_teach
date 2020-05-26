from flask import Blueprint,request, jsonify
from myapp.models import User, db
from myapp.front.auth import login_required

front = Blueprint("front",__name__)


@front.route("/")
@login_required
def hello(userid):
    return "Hello admin"+userid

