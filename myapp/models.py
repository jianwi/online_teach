from myapp import db
from datetime import datetime

user_course_table = db.Table('user_course',
                             db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                             db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
                             )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    sex = db.Column(db.String(10))
    age = db.Column(db.Integer)
    account = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    describe = db.Column(db.Text)
    created_at = db.Column(db.DateTime,default=datetime.now())
    courses = db.relationship("Course", secondary=user_course_table)


    def to_json(self):
        return {
            "id": self.id,
            "account": self.account,
            "name" : self.name,
            "avatar": self.avatar,
            "sex": self.sex,
            "age": self.age,
            "describe": self.describe,
            "created_at": self.created_at
        }


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    account = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    phone_number = db.Column(db.String(30))
    institution = db.Column(db.String(255))
    post_num = db.Column(db.Integer,default=0)
    created_at = db.Column(db.DateTime,default=datetime.now())
    courses = db.relationship('Course')

    def to_json(self):
        return {
            "id": self.id,
            "account": self.account,
            "name": self.name,
            "avatar": self.avatar,
            "phone_number": self.phone_number,
            "created_at": self.created_at,
            "post_num": self.post_num
        }


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    content = db.Column(db.Text)
    videos = db.Column(db.Text)
    type = db.Column(db.Integer)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    cover = db.Column(db.String(255))
    collect_num = db.Column(db.Integer,default=0)
    view_num = db.Column(db.Integer,default=0)
    score = db.Column(db.Integer,default=0)
    created_at = db.Column(db.DateTime,default=datetime.now())
    module = db.relationship('Module')
    admin = db.relationship("Admin")
    users = db.relationship("User",secondary=user_course_table)

    def to_json(self):
        return {
            "id": self.id,
            "name" : self.name,
            "admin" : self.admin.to_json(),
            "content": self.content,
            "videos": self.videos,
            "type": self.type,
            "module": self.module.name,
            "score": self.score,
            "view_num": self.view_num,
            "collect_num": self.collect_num,
            "created_at": self.created_at,
            "cover": self.cover
        }


class Module(db.Model):
    __tablename__ = "modules"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    courses = db.relationship("Course")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Scores(db.Model):
    __tablename__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    score = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    user = db.relationship("User")
    course = db.relationship("Course")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.Integer)
    from_user_type = db.Column(db.Integer)
    to_user_id = db.Column(db.Integer)
    to_user_type = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime,default=datetime.now())
    course = db.relationship("Course")

    def to_json(self):
        if self.from_user_type == 1:
            from_user = User.query.get(self.from_user_id).to_json()
        else:
            from_user = Admin.query.get(self.from_user_id).to_json()
        if self.to_user_type == 1:
            to_user = User.query.get(self.to_user_id).to_json()
        else:
            to_user = Admin.query.get(self.to_user_id).to_json()

        return {
            'id': self.id,
            "from_user": from_user,
            "to_user": to_user,
            "content": self.content,
            "course": self.course.to_json(),
            "created_at": self.created_at
        }



class UserSearchHistory(db.Model):
    __tablename__ = "user_search_histories"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    content = db.Column(db.Text,unique=True)
    created_at = db.Column(db.DateTime,default=datetime.now())



