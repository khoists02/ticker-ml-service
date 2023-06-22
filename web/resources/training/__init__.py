from flask_restful import Resource
from traning.stock import StockTraining
import os

ROOT_DIR = os.path.abspath(os.curdir)


class TrainingResource(Resource):
    def get(self):
        dir = os.path.join(ROOT_DIR, 'web', 'data', 'test.csv')
        stock = StockTraining(dir)
        stock.run()
        predict = stock.prediction()
        return {"predict": str(predict)}
