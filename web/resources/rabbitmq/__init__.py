# from rabbitmq.consumer import main, data
import json
import pika
import time
import threading
from config import AppConfig
from flask_restful import Resource
from flask import abort
from model.stock import StockDto
from rabbitmq.publisher import PikaPublisher
from rabbitmq.ticker import Ticker
import json
import errors
import logging
logger = logging.getLogger('ftpuploader')

appConfig = AppConfig()

data = []


# class RabbitMQReceived(Resource):
#     def callback(ch, method, properties, body):
#         print(body)
#         data.append(body)
#         ch.basic_ack(delivery_tag=method.delivery_tag)

#     def get(self):
#         try:
#             parameters = pika.URLParameters(appConfig.RABBITMQ_HOST)
#             connection = pika.BlockingConnection(parameters)
#             channel = connection.channel()
#             channel.queue_declare(
#                 queue=appConfig.RABBITMQ_QUEUE)
#             channel.basic_qos(prefetch_count=1)
#             channel.basic_consume(queue=appConfig.RABBITMQ_QUEUE,
#                                   on_message_callback=self.callback)
#             channel.start_consuming()

#             return {"test": "a"}
#         except Exception as e:
#             abort(500, errors.internal_err)


class RabbitMQ(Resource):
    def get(self):
        try:
            stock_ob = StockDto()
            stock_ob.close = "1"
            stock_ob.volume = "1"
            stock_ob.low = "1"
            stock_ob.high = "1"
            stock_ob.close = "1"
            stock_ob.date = "1"
            publisher = PikaPublisher(
                exchange_name=appConfig.RABBITMQ_EXCHANGE)
            ticker = Ticker(
                publisher=publisher,
                qname=appConfig.RABBITMQ_QUEUE,
                json_message=json.dumps(stock_ob.__dict__)
            )
            ticker.monitor()

            return json.dumps(stock_ob.__dict__)
        except Exception as e:
            print(str(e))
            abort(500, errors.internal_err)
