from flask_restful import Resource
from rabbitmq.publisher import PikaPublisher
from rabbitmq.consumer import PikaConsumer


class Received(Resource):
    def get(self):
        publisher = PikaPublisher(exchange_name="stock")
        consumer = PikaConsumer(publisher=publisher, qname="report-stock")
        consumer.received()
        return {"received": "A"}
