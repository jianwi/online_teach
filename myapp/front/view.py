from flask import Blueprint, request, jsonify
from myapp.models import User, db, Scores, Course, Comment, UserSearchHistory
from myapp.front.auth import login_required
from myapp.api.resp import Resp

front = Blueprint("front", __name__)


@front.route("/")
@login_required
def hello(userid):
    return "Hello admin" + userid


@front.route("course/star/get/<course_id>")
@login_required
def get_course_score(userid, course_id):
    score = Scores.query.filter_by(user_id=userid, course_id=course_id).first()
    if score:
        return Resp.success(data=score.score)
    else:
        return Resp.error()


@front.route("course/star/post/<course_id>/<score>", methods=['POST'])
@login_required
def give_course_score(userid, course_id, score):
    score_all = Scores.query.filter_by(course_id=course_id).all()
    has_score = Scores.query.filter_by(user_id=userid, course_id=course_id).first()
    course = Course.query.get(course_id)

    if not has_score:
        score_new = Scores(user_id=userid, course_id=course_id, score=score)
        score_time = len(score_all)
        if score_time == 0:
            course.score = score
        else:
            course.score = (course.score + score) / (score_time + 1)
        db.session.add(score_new)
        db.session.commit()
        return Resp.success()
    else:
        return Resp.error(message="已经打过分了")


# 添加评论
@front.route("course/comment/add", methods=['POST'])
@login_required
def add_comment(userid):
    course_id = request.get_json()['course_id']
    content = request.get_json()['content']
    course = Course.query.get(course_id)

    comment_new = Comment(
        course_id=course_id,
        content=content,
        from_user_id=userid,
        from_user_type=1,
        to_user_id=course.admin_id,
        to_user_type=2
    )

    db.session.add(comment_new)
    db.session.commit()

    return Resp.success()


# 收藏课程
@front.route("course/love/<course_id>", methods=["POST"])
@login_required
def user_love_course(userid, course_id):
    user = User.query.get(userid)
    course = Course.query.get(course_id)
    if not course in user.courses:
        user.courses.append(course)
        course.collect_num = len(course.users)
        db.session.commit()
        return Resp.success()
    else:
        return Resp.error()


@front.route("course/loved/<course_id>")
@login_required
def is_my_loved_course(userid, course_id):
    user = User.query.get(userid)
    course = Course.query.get(course_id)
    if course in user.courses:
        print("yes i loved it")
        return Resp.success(data="true")
    else:
        return Resp.success(data="false")


@front.route("course/dontlove/<course_id>", methods=["POST"])
@login_required
def dont_love_it_anymore(userid, course_id):
    user = User.query.get(userid)
    course = Course.query.get(course_id)
    user.courses.remove(course)
    course.collect_num = len(course.users)
    db.session.commit()
    return Resp.success()


# 用户个人信息
@front.route("user/info")
@login_required
def user_infos(userid):
    user = User.query.get(userid)
    return Resp.success(data=user.to_json())


# 修改头像
@front.route("user/info/avatar/change/<file_name>", methods=['POST'])
@login_required
def user_info(userid, file_name):
    user = User.query.get(userid)
    user.avatar = file_name
    db.session.commit()
    return Resp.success()


# 收藏列表
@front.route("course/loved/all/list")
@login_required
def all_my_loved_course(userid):
    user = User.query.get(userid)
    courses = user.courses

    return Resp.success(data=[
        course.to_json() for course in courses
    ])


# 评论列表
@front.route("my/comments/list")
@login_required
def my_comments_list(userid):
    user = User.query.get(userid)
    comments = Comment.query.filter_by(from_user_id=userid, from_user_type=1).all()
    return Resp.success(data=[
        comment.to_json() for comment in comments
    ])


# 回复我的
@front.route("my/reply/list")
@login_required
def my_replies_lists(userid):
    user = User.query.get(userid)
    comments = Comment.query.filter_by(to_user_id=userid, from_user_type=2).all()
    return Resp.success(data=[
        comment.to_json() for comment in comments
    ])


# 修改信息
@front.route("my/info/modify", methods=['POST'])
@login_required
def modify_user_info(userid):
    data = request.get_json()
    user = User.query.get(userid)

    user.name = data['name']
    user.sex = data['sex']
    user.age = data['age']
    user.describe = data['describe']
    if data['password'] != "":
        print("修改密码了")
        user.password = data['password']

    db.session.commit()
    return Resp.success()


# 搜索历史
@front.route("my/search/history")
@login_required
def search_history(userid):
    histories = UserSearchHistory.query.filter_by(user_id=userid).all()
    return Resp.success(data=[
        history.content for history in histories
    ])


# 搜索课程
@front.route("course/filter/<key>")
@login_required
def search_course_by_name(userid,key):
    h = UserSearchHistory(
        user_id=userid,
        content=key
    )
    db.session.add(h)
    db.session.commit()
    courses = Course.query.filter(Course.name.like('%'+key+'%')).all()
    return Resp.success(data=[course.to_json() for course in courses])
