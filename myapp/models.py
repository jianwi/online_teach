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
            "account": self.account,
            "name": self.name,
            "avatar": self.avatar,
            "phone_number": self.phone_number,
            "created_at": self.created_at
        }


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    content = db.Column(db.Text)
    videos = db.Column(db.Text)
    type = db.Column(db.Integer)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    cover = db.Column(db.String(255))
    collect_num = db.Column(db.Integer)
    view_num = db.Column(db.Integer)
    score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime,default=datetime.now())
    module = db.relationship('Module')
    users = db.relationship("User",secondary=user_course_table)


class Module(db.Model):
    __tablename__ = "modules"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    courses = db.relationship("Course")


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
    To_user_type = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime,default=datetime.now())



class UserSearchHistory(db.Model):
    __tablename__ = "user_search_histories"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime,default=datetime.now())



