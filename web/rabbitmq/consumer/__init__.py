import pika
from config import AppConfig
from flask import abort

appConfig = AppConfig()


def worker():
    print(' Connecting to server ...')

    try:
        params = pika.URLParameters(appConfig.RABBITMQ_HOST)
        connection = pika.BlockingConnection(params)
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return

    channel = connection.channel()
    channel.queue_declare(queue=appConfig.RABBITMQ_QUEUE)

    # channel.queue_bind(queue=appConfig.RABBITMQ_QUEUE,
    #                    routing_key=appConfig.RABBITMQ_ROUTINGKEY, exchange=appConfig.RABBITMQ_EXCHANGE)

    print(' Waiting for messages...')

    def callback(ch, method, properties, body):
        print(" Received %s" % body.decode())
        print(" Done")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=appConfig.RABBITMQ_QUEUE,
                          on_message_callback=callback)
    channel.start_consuming()
