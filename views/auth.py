from flask import jsonify,request,abort
from app import app


@app.route('/login')
def login():
    return abort(403)