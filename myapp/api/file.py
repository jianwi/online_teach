import uuid
from flask import request, jsonify, send_from_directory, Blueprint
from config import Config
import os

file = Blueprint("upload", __name__)


@file.route('/get/<filename>')
def get_img(filename):
    return send_from_directory(Config.UPLOAD_FOLDER,filename)


@file.route('/upload/',methods=['POST'])
def upload():
    image = request.files.get('file')
    if image:
        if not image.filename.endswith(tuple(['.jpg','.png','.mp4'])):
            return jsonify({'message':'error file format'}),409

        print(uuid.uuid4())

        filename = str(uuid.uuid4()).replace('-','') + '.' + image.filename.split('.')[-1]

        if not os.path.isdir(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
        image.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        return filename
    else:
        return "nothing upload"
