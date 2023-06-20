from flask_restful import Resource
from flask import jsonify

class Ticker(Resource):
    def get(self): return jsonify({'ticker': 'None'})