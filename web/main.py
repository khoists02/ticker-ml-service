
from main import app
import pika
from rabbitmq.consumer import worker
from config import AppConfig
import sys
import threading
import os

appConfig = AppConfig()


def start_rmq_connection():
    # Connection
    params = pika.URLParameters(appConfig.RABBITMQ_HOST)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    # Exchange and queues
    channel = connection.channel()
    channel.queue_declare(queue=appConfig.RABBITMQ_QUEUE)

    def callback(ch, method, properties, body):
        print("**************************************")
        print(method)
        print(" Received %s" % body.decode())
        print(" Done")
        print("**************************************")
        # ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=appConfig.RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages.')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        # thread_1 = threading.Thread(target=start_rmq_connection)
        # thread_1.start()
        # thread_1.join(0)
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
