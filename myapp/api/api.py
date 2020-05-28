from flask import Blueprint, request, jsonify
from myapp.models import Module, db, Course
from myapp.api.resp import Resp

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
    return Resp.success(data=course.to_json())


@api.route("/course/all")
def all_course():
    courses = Course.query.all()
    return Resp.success(data=[course.to_json() for course in courses])