import os

base_url = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://online_teach:online_teach@localhost/online_teach'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DATABASE_URI = 'mysql+pymysql://online_teach:online_teach@localhost/online_teach'

    #  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_url,'data.sql')