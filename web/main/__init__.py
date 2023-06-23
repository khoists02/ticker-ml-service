from flask import Flask, jsonify
from flask_restful import Api
from resources.user import User
from resources.trainmodel import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from config import AppConfig
from database import db
from werkzeug import exceptions

# Configuration Application
appConfig = AppConfig()
app = Flask(__name__)
api = Api(app)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = appConfig.SQLALCHEMY_DATABASE_URI
db.init_app(app)

# APIs
api.add_resource(User, '/api/user')
api.add_resource(TrainingResource, '/api/train/<string:id>')
api.add_resource(RabbitMQ, '/api/send')
api.add_resource(Received, '/api/received')


# Error Defined
@app.errorhandler(exceptions.BadRequest)
def handle_bad_request_exception(e):
    return jsonify({
        "code": e.code,
        "name": e.name
    }), 400


@app.errorhandler(exceptions.InternalServerError)
def handle_internal_server_error_exception(e):
    return jsonify({
        "code": e.code,
        "name": e.name
    }), 500


# Error Handling
app.register_error_handler(400, handle_bad_request_exception)
app.register_error_handler(500, handle_internal_server_error_exception)
