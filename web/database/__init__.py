
import psycopg2

# jdbc:postgresql://localhost:5439/tickers


class DatabaseConfig:
    def __init__(self, url='') -> None:
        self.conn = psycopg2.connect(database="tickers", user="advax",
                                     password="advax", host="localhost", port="5439")
        self.cur = self.conn.cursor()
        self.url = url

    def connect(self):
        pass

    def get_cursor(self):
        return self.cur

    def close(self):
        self.cur.close()
        self.conn.close()
