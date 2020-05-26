from flask import Blueprint,request, jsonify
from myapp.models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

front = Blueprint("front",__name__)

@front.route("/")
def hello():
    return "Hello admin"


@front.route("/r",methods=['post'])
def register():
    if not request.form.get("account"):
        return jsonify({"message": "account not specified"}), 409
    if not request.form.get("password"):
        return jsonify({"message": "Password not specified"}), 409

    if User.query.filter_by(account=request.form.get("account")).first():
        return jsonify({"message": "account not available"}), 409

        # Hash password with sha256
    hashed_password = generate_password_hash(request.form.get("password"))

    try:
        user = User(
        account=request.form.get("account"),
        password=hashed_password)

        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({"message": "something wrong"}), 501

    return jsonify({"message": "register success"})
