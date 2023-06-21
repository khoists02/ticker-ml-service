from flask_restful import Resource
from traning.stock import StockTraining


class TrainingResource(Resource):
    def get_prediction(self):
        StockTraining.run()
        predict = StockTraining.prediction()
        return { predict }