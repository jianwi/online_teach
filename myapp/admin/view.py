from flask import Blueprint,request, jsonify
from myapp.models import Admin, db,Course, Module
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


@admin.route("/user/info")
@login_required
def user_info(userid):
    admin = Admin.query.get(userid)
    return Resp.success(data=admin.to_json())


@admin.route("/user/all")
def user_all():
    admins = Admin.query.all()
    return jsonify([admin.to_json() for admin in admins])


@admin.route("/course/add",methods=['POST'])
@login_required
def course_store(userid):
    form_data = request.get_json()
    module_name = form_data['module']
    module_db = Module.query.filter_by(name=module_name).first()
    if module_db:
        module_id = module_db.id
    else:
        module_new = Module(
            name=module_name
        )
        db.session.add(module_new)
        db.session.commit()
        module_id = module_new.id

    course_new = Course(
        name=form_data['name'],
        cover=form_data['cover'],
        module_id=module_id,
        content=form_data['content'],
        type=form_data['type'],
        admin_id=userid
    )
    db.session.add(course_new)
    db.session.commit()
    return Resp.success()


@admin.route("/course/edit/<id>",methods=["POST"])
@login_required
def course_edit(userid,id):
    course = Course.query.get(id)
    form_data = request.get_json()

    module_name = form_data['module']
    module_db = Module.query.filter_by(name=module_name).first()
    if module_db:
        module_id = module_db.id
    else:
        module_new = Module(
            name=module_name
        )
        db.session.add(module_new)
        db.session.commit()
        module_id = module_new.id

    course.name = form_data['name']
    course.cover = form_data['cover']
    course.module_id = module_id
    course.content = form_data['content']
    course.type = form_data['type']
    db.session.commit()
    return Resp.success()

@admin.route("/course/list")
@login_required
def course_list(userid):
    list = Admin.query.get(userid).courses
    return Resp.success(data=[
        course.to_json() for course in list
    ])


@admin.route("/course/delete/<id>",methods=["POST"])
@login_required
def course_delete(userid,id):
    course = Course.query.filter_by(id=id,admin_id=userid).first()
    if not course:
        return Resp.error(message="这个课程不是你创建的，你没有权限删除它")
    else:
        db.session.delete(course)
        db.session.commit()
        return Resp.success()