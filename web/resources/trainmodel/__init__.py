from flask_restful import Resource
from train.stock import StockTraining
import os
from flask import request
from config import AppConfig

appConfig = AppConfig()


class TrainingResource(Resource):
    def get(self):
        print(request.base_url)
        base_url = request.base_url
        dir = ''
        if appConfig.APP_URL in base_url:  # Run On Docker
            dir = os.path.join(appConfig.ROOT_DIR, 'test.csv')
        else:
            dir = os.path.join(appConfig.ROOT_DIR, 'web', 'data', 'test.csv')
        print(dir)

        stock = StockTraining(dir)
        stock.run()
        predict = stock.prediction()
        return {"predict": str(predict)}
