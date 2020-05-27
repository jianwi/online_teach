from flask import Blueprint,request, jsonify
from myapp.models import Admin, db
from myapp.admin.auth import login_required
from myapp.api.resp import Resp

admin = Blueprint("admin",__name__)


@admin.route("/")
@login_required
def hello(userid):
    return "Hello admin"+userid


@admin.route("/complete_info",methods=['POST'])
@login_required
def complete_info(userid):
    form_data = request.get_json()
    admin = Admin.query.get(userid)
    admin.name = form_data['name']
    admin.avatar = form_data['avatar']
    admin.phone_number = form_data['phone_number']
    admin.institution = form_data['institution']
    db.session.commit()
    return Resp.success()