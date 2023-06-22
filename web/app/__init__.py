from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import User
from resources.trainmodel import TrainingResource
from resources.rabbitmq import RabbitMQ
from resources.received import Received
from config import AppConfig
from sqlalchemy import text
from database import db
from model.tickers_stock import TickersStock

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
    con = db.session.connection()
    # query = text(
    #     "select * from tickers_stock ")
    # result = con.execute(query).first()
    # print(result)

    query = db.session.query(TickersStock).filter(
        TickersStock.id == "73929f93-1deb-4543-afff-a63a26281771")
    # result = con.execute(text(query)).first()
    print(query)

    for i in query:
        print(i.ticker_attributes_json)

    return "Home Page !!!"
