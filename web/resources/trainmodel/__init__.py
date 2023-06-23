from flask_restful import Resource
from train.stock import StockTraining
import json
from database import db
from model.tickers_stock import TickersStockQuery
from config import AppConfig
from model.dto.stock_train import StockTrain
from flask import abort
import errors
from model.tickers_stock import TickersStock

appConfig = AppConfig()


class TrainingResource(Resource):
    def post(self, id: str):
        if (id is None):
            abort(400, errors.not_found_err)
        # query instance of model
        qr = TickersStockQuery()

        # run query
        item: TickersStock = qr.findOneById(value=id)

        print(item)
        if (item is None):
            abort(400, errors.not_found_err)

        # convert to object
        data = json.loads(item.ticker_attributes_json,
                          object_hook=lambda d: StockTrain(**d))

        max_len = len(data) - 1

        for index, dt in enumerate(data):
            stock: StockTrain = dt
            stock.volume = int(stock.volume.replace(",", "")
                               ) if stock.volume != "" else 0
            stock.open = float(stock.open) if stock.open != "" else 0
            stock.close = float(stock.close) if stock.close != "" else 0
            stock.high = float(stock.high) if stock.high != "" else 0
            stock.low = float(stock.low) if stock.low != "" else 0
            stock.date = str(stock.date)

            if index < max_len:
                if (float(data[index].close)) <= float(data[index + 1].close):
                    stock.higher = 0
                else:
                    stock.higher = 1

        data_train_json = json.dumps(data, default=lambda o: o.__dict__)

        # Run Stock Data
        stock = StockTraining(data_train_json)
        stock.run()
        predict = stock.prediction()
        return {"predict": str(predict)}
