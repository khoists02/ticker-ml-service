# example_consumer.py
import pika
import os
import time


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


class PikaConsumer:
    def __init__(self, publisher, qname) -> None:
        self.publisher = publisher
        self.qname = qname

    def received(self):
        self.publisher.monitor(qname=self.qname, callback=callback)
