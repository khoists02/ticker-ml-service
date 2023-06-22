from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import User
from resources.training import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from database import DatabaseConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()
# config = DatabaseConfig(url='')
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://advax:advax@localhost:5439/tickers"
api = Api(app)
# rabbit = RabbitMQ(app, 'report-stock')
db.init_app(app)


# api.add_resource(Auth, '/api/auth')
api.add_resource(User, '/api/user')
api.add_resource(TrainingResource, '/api/train')
api.add_resource(RabbitMQ, '/api/send')
api.add_resource(Received, '/api/received')


@app.route('/')
def home():
    con = db.session.connection()
    query = text("select * from tickers")
    result = con.execute(query)
    print(result)
    return "Home"

# @app.route('ping', methods=['GET'])
# def ping():
#     rabbit.send(body='ping', routing_key='ping.message')
#     return 'pong'

# # listen to messages


# @rabbit.queue(routing_key='ping.message')
# def ping_event(routing_key, body):
#     app.logger.info('Message received:')
#     app.logger.info('\tKey: {}'.format(routing_key))
#     app.logger.info('\tBody: {}'.format(body))
