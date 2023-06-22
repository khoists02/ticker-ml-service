import json
import random
from flask import jsonify


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

    # def get_quote(self):
    #     symbol = random.choice(self.stock_symbols)
    #     if symbol in self.last_quote:
    #         previous_quote = self.last_quote[symbol]
    #         new_quote = random.uniform(0.9*previous_quote, 1.1*previous_quote)
    #         if abs(new_quote) - 0 < 1.0:
    #             new_quote = 1.0
    #         self.last_quote[symbol] = new_quote
    #     else:
    #         new_quote = random.uniform(10.0, 250.0)
    #         self.last_quote[symbol] = new_quote
    #     self.counter += 1
    #     return (symbol, self.last_quote[symbol], time.gmtime(), self.counter)

    def monitor(self):

        self.publisher.publish(self.json_message, routing_key="rabbitmq.*")
        # while True:
        #     quote = self.get_quote()
        #     print("New quote is %s" % str(quote))

        #     secs = random.uniform(0.1, 0.5)
        #     # print("Sleeping %s seconds..." % secs)
        #     time.sleep(secs)
