from flask import Flask, abort, jsonify
from flask_restful import Api
from resources.user import User
from resources.trainmodel import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from config import AppConfig
from database import db
from error import Error
from werkzeug import exceptions
import json

not_found_err = Error(code=400, name='Error',
                      description='Bad Request')

appConfig = AppConfig()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = appConfig.SQLALCHEMY_DATABASE_URI
db.init_app(app)

api.add_resource(User, '/api/user')
api.add_resource(TrainingResource, '/api/train')
api.add_resource(RabbitMQ, '/api/send')
api.add_resource(Received, '/api/received')


@app.errorhandler(exceptions.BadRequest)
def handle_bad_request_exception(e):
    return jsonify({
        "code": e.code,
        "name": e.name
    })


# @app.errorhandler(HTTPException)
# def handle_exception(e: Error):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     }, default=lambda o: o.__dict__)
#     response.content_type = "application/json"
#     return response


app.register_error_handler(400, handle_bad_request_exception)
# app.register_error_handler(500, handle_exception)


@app.route('/')
def home():
    if db is not None:
        abort(400, not_found_err)
    db.session.connection()

    return {}
