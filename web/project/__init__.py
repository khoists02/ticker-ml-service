from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import User

class Auth(Resource):
   def get(self): return {};

app = Flask(__name__)
api = Api(app)

api.add_resource(Auth, '/api/auth')
api.add_resource(User, '/api/user')