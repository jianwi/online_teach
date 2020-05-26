from flask import Blueprint, request, jsonify
from myapp.models import User, db
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import Config

front_auth = Blueprint("front_auth", __name__)


# 登录验证
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            # Check whether token was sent
            authorization_header = request.headers["Authorization"]

            # Check whether token is valid
            try:
                token = authorization_header.split(" ")[1]
                user = jwt.decode(token, Config.SECRET_KEY)
            except:
                return jsonify({"message": "you are not logged in"}), 401

            return f(userid=user["userid"], *args, **kwargs)
        else:
            return jsonify({"message": "you are not logged in"}), 401
    return wrap


# 用户注册
@front_auth.route("/register", methods=['post'])
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


# 登录
@front_auth.route('/login', methods=['POST'])
def login():
    if not request.form.get("account"):
        return jsonify({"message": "account not specified"}), 409
    if not request.form.get("password"):
        return jsonify({"message": "Password not specified"}), 409

    try:
        account = request.form.get("account")
        user = User.query.filter_by(account=request.form.get("account")).first()
    except:
        return jsonify("database error"),501

    if user == None:
        return jsonify({"message": "User not found"}), 403

    if not check_password_hash(user.password, request.form.get("password")):
        return jsonify({"message": "Invalid password"}), 401

    token = jwt.encode({
        "userid": str(user.id),
        "account": user.account,
        "password": user.password,
        "created": str(user.created_at)
    }, Config.SECRET_KEY)

    return jsonify({
        "message": '登录成功',
        "data": {
            "user": user.to_json(),
            "token": token.decode("UTF-8"),
        },
    })
