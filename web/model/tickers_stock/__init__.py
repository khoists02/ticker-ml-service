from sqlalchemy import Column, UUID, String
from database import db


class TickersStock(db.Model):
    id = Column(UUID, primary_key=True)
    ticker_name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    ticker_attributes_json = Column(String, nullable=True)
    file_name = Column(String, nullable=True)

    def __repr__(self):
        return '<TickersStock %r>' % self.ticker_name
