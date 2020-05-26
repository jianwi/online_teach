from app import db

ass = db.Table('ass',
                             db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id')),
                             db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
                             )


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    teachers = db.relationship('Teacher',
                               secondary=ass)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    students = db.relationship('Student', secondary=ass)