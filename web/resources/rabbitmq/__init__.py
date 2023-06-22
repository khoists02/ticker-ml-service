from flask_restful import Resource
from model.stock import StockDto
from rabbitmq.publisher import PikaPublisher
from rabbitmq.ticker import Ticker
import json


class RabbitMQ(Resource):
    def get(self):
        stock_ob = StockDto()
        stock_ob.close = "1"
        stock_ob.volume = "1"
        stock_ob.low = "1"
        stock_ob.high = "1"
        stock_ob.close = "1"
        stock_ob.date = "1"
        publisher = PikaPublisher(exchange_name="stock")
        ticker = Ticker(publisher=publisher,
                        qname="report-stock", json_message=json.dumps(stock_ob.__dict__))
        ticker.monitor()
        return "success !!"
