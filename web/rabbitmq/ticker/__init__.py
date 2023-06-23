import random
from config import AppConfig

appConfig = AppConfig()


class Ticker(object):
    def __init__(self, publisher, qname, json_message):
        self.publisher = publisher
        self.json_message = json_message
        # This quickly creates four random stock symbols
        chars = range(ord("A"), ord("Z")+1)
        def random_letter(): return chr(random.choice(chars))
        self.stock_symbols = [
            random_letter()+random_letter()+random_letter() for i in range(4)]

        self.last_quote = {}
        self.counter = 0
        self.time_format = "%a, %d %b %Y %H:%M:%S +0000"
        self.qname = qname

    def monitor(self):
        self.publisher.publish(
            self.json_message, routing_key=appConfig.RABBITMQ_ROUTINGKEY)
