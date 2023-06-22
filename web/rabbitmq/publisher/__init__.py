import pika
import json


class PikaPublisher(object):
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.queue_exists = False

    def publish(self, message, routing_key):
        url = 'amqp://guest:guest@localhost:5672/%2f'
        params = pika.URLParameters(url)
        print(self.exchange_name)
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

    def monitor(self, qname, callback):
        url = 'amqp://guest:guest@localhost:5672/%2f'
        params = pika.URLParameters(url)
        print(params)
        connection = pika.BlockingConnection(params)
        print("pass con")

        ch = connection.channel()

        print("start channel")
        ch.queue_declare(queue=qname, durable=True,
                         exclusive=False, auto_delete=False)

        ch.basic_consume(
            queue=qname, on_message_callback=callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        ch.start_consuming()
