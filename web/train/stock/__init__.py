import tensorflow as tf
import pandas as pd


class StockTraining:
    def __init__(self, json):
        self.json = json
        self.FLOATS_COLUMNS = ['open', 'close', 'high', 'low']
        self.NUMBERS_COLUMNS = ['volume']
        self.CATEGORICAL_COLUMNS = ['date']
        self.feature_columns = []
        self.y_stock_train = []
        self.y_stock_test = []
        self.stock_data = []
        self.stock_data_test = []

    def get_data_training(self):
        data = pd.read_json(self.json)
        # convert pandas date to str
        data['date'] = pd.to_datetime(data['date'].astype(str),
                                      errors='coerce',
                                      exact='True',
                                      format='%Y-%m-%d'  # provide your format here
                                      )
        data['date'] = data['date'].astype(str)
        # Train Data
        self.stock_data = data
        self.stock_data_test = data[:10]

        self.y_stock_train = self.stock_data.pop("higher")
        self.y_stock_test = self.stock_data_test.pop("higher")

    def get_features(self):
        # pass
        for feature_name in self.CATEGORICAL_COLUMNS:
            # gets a list of all unique values from given feature column
            vocabulary = self.stock_data[feature_name].unique()
            self.feature_columns.append(
                tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary, dtype=None))

        for feature_name in self.FLOATS_COLUMNS:
            self.feature_columns.append(
                tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

        for feature_name in self.NUMBERS_COLUMNS:
            self.feature_columns.append(
                tf.feature_column.numeric_column(feature_name, dtype=tf.int32))

    def make_input_fn(self, data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
        def input_function():  # inner function, this will be returned
            # create tf.data.Dataset object with data and its label
            ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
            if shuffle:
                ds = ds.shuffle(1000)  # randomize order of data
            # split dataset into batches of 32 and repeat process for number of epochs
            ds = ds.batch(batch_size).repeat(num_epochs)
            return ds  # return a batch of the dataset
        return input_function  # return a function object for use

    def get_train_input_fn(self):
        return self.make_input_fn(self.stock_data, self.y_stock_train)

    def get_eval_input_fn(self):
        return self.make_input_fn(self.stock_data_test, self.y_stock_test, num_epochs=1, shuffle=False)

    def prediction(self) -> float:
        linear_est = tf.estimator.LinearClassifier(
            feature_columns=self.feature_columns)
        linear_est.train(self.get_train_input_fn())  # train
        # get model metrics/stats by testing on testing data
        result = linear_est.evaluate(self.get_eval_input_fn())
        return result['accuracy']

    def run(self) -> None:
        self.get_data_training()
        self.get_features()
        # self.get_train_input_fn()
        # self.get_eval_input_fn()
