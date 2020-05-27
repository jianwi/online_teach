from flask import jsonify


class Resp:
    def success(message="success",data={}):
        return jsonify({
            "code" : 200,
            "message": message,
            "data" : data
        })

    def error(message="fail",code="555"):
        return jsonify({
            "code": code,
            "message": message
        })