from flask import Blueprint, request, jsonify
from myapp.models import Module, db, Course, Comment
from myapp.api.resp import Resp
from sqlalchemy import desc
from sqlalchemy.sql.expression import func


api = Blueprint("api", __name__)


@api.route("/modules")
def modules():
    all_module = Module.query.all()
    return Resp.success(data=[{
        "value": module.name
    } for module in all_module])


@api.route("/course/get/<id>")
def get_course(id):
    course = Course.query.get(id)
    course.view_num = 1 if course.view_num==None else course.view_num+1
    return Resp.success(data=course.to_json())


@api.route("/course/all")
def all_course():
    courses = Course.query.all()
    return Resp.success(data=[course.to_json() for course in courses])


@api.route("/comment/all/<course_id>")
def get_comments(course_id):
    comments = Comment.query.filter_by(course_id=course_id).all()
    list = [
        comment.to_json() for comment in comments
    ]
    return  Resp.success(data=list)


@api.route("/comment/get/<id>")
def get_comment(id):
    comment = Comment.query.get(id)
    return Resp.success(data=comment.content)


# 根据模块获取课程
@api.route("course/get/from/module/<module>")
def get_courses_form_module(module):
    if module=="1":
        courses = Course.query.order_by(desc('view_num')).all()
    elif module=="2":
        courses = Course.query.order_by(func.random()).limit(5).all()
    else:
        module = Module.query.filter_by(name=module).first()
        courses = Course.query.filter_by(module=module).all()
    print(courses)
    return Resp.success(data=[course.to_json() for course in courses])


