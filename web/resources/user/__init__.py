from flask_restful import Resource
from flask import jsonify

class User(Resource):
    def get(self): return jsonify({'username': 'khoile'})