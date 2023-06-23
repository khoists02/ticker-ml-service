from flask import Flask, jsonify
import array as arr
from flask_restful import Api, Resource
from resources.user import User
from resources.trainmodel import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from config import AppConfig
from database import db
from model.tickers_stock import TickersStockQuery
import json
from model.dto.stock_train import StockTrain

appConfig = AppConfig()

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = appConfig.SQLALCHEMY_DATABASE_URI
db.init_app(app)

api.add_resource(User, '/api/user')
api.add_resource(TrainingResource, '/api/train')
api.add_resource(RabbitMQ, '/api/send')
api.add_resource(Received, '/api/received')


@app.route('/')
def home():
    db.session.connection()

    return {}
