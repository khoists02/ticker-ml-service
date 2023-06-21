from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import User
from resources.training import TrainingResource

class Auth(Resource):
   def get(self): return {}

app = Flask(__name__, static_folder='web/data')
api = Api(app)

api.add_resource(Auth, '/api/auth')
api.add_resource(User, '/api/user')
api.add_resource(TrainingResource, '/api/train')