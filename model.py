from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True)
  password = Column(String)
  role = Column(String)


class Shoe(Base):
  __tablename__ = "shoes"
  id = Column(Integer, primary_key=True)
  brand = Column(String)
  size = Column(Integer)
  price = Column(Integer)
  stock = Column(Integer)


class Sale(Base):
  __tablename__ = "sales"
  id = Column(Integer, primary_key=True)
  shoe_id = Column(Integer, ForeignKey("shoes.id"))
  buyer_name = Column(String)
  pairs = Column(Integer)
  total_price = Column(Integer)


class StockLog(Base):
  __tablename__ = "stock_logs"
  id = Column(Integer, primary_key=True)
  shoe_id = Column(Integer, ForeignKey("shoes.id"))
  staff_name = Column(String)
  added_pairs = Column(Integer)
  new_stock = Column(Integer)