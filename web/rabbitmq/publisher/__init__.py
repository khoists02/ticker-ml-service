import pika
import json
from config import AppConfig
from flask import abort
import errors

appConfig = AppConfig()


class PikaPublisher(object):
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.queue_exists = False

    def publish(self, message, routing_key):
        try:
            print("start connection", appConfig.RABBITMQ_HOST)
            params = pika.URLParameters(appConfig.RABBITMQ_HOST)
            print("start connection", params)
            connection = pika.BlockingConnection(params)
            ch = connection.channel()

            ch.exchange_declare(exchange=self.exchange_name,
                                exchange_type="direct", durable=True, auto_delete=False)

            print("Send message ," + message)

            ch.basic_publish(exchange=self.exchange_name,
                             routing_key=routing_key,
                             body=json.dumps(message),
                             properties=pika.BasicProperties(
                                 delivery_mode=2,  # persistent
                             ))
            ch.close()
            connection.close()
        except Exception:
            abort(500, errors.internal_err)

    def monitor(self, qname, callback):
        params = pika.URLParameters(appConfig.RABBITMQ_HOST)
        connection = pika.BlockingConnection(params)
        ch = connection.channel()

        print("start channel")
        ch.queue_declare(queue=qname, durable=True,
                         exclusive=False, auto_delete=False)

        ch.basic_consume(
            queue=qname, on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        ch.start_consuming()
