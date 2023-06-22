from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import User
from resources.trainmodel import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from database import DatabaseConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import AppConfig

config = AppConfig()
db = SQLAlchemy()
app = Flask(__name__)
print("DATABASE URL", config.SQLALCHEMY_DATABASE_URI)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
api = Api(app)
db.init_app(app)


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
