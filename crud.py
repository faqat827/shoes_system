import os
from database import Base, SessionLocal, engine
from dotenv import load_dotenv
from model import Sale, Shoe, StockLog, User

load_dotenv()

admin_pass = os.getenv("ADMIN_PASSWORD", "123")
staff_pass = os.getenv("STAFF_PASSWORD", "123")
buyer_pass = os.getenv("BUYER_PASSWORD", "123")

Base.metadata.create_all(bind=engine)


def setup_default_data():
  db = SessionLocal()

  defaults = [
      ("admin", admin_pass, "admin"),
      ("staff", staff_pass, "staff"),
      ("buyer", buyer_pass, "buyer"),
  ]

  for name, pwd, role in defaults:
    user = db.query(User).filter(User.username == name).first()
    if user:
      user.password = pwd
      user.role = role
    else:
      db.add(User(username=name, password=pwd, role=role))

  for size in range(1, 11):
    shoe = db.query(Shoe).filter(Shoe.size == size).first()
    if not shoe:
      db.add(Shoe(brand="Bata", size=size, price=2500, stock=10))

  db.commit()
  db.close()


def login(username, password):
  db = SessionLocal()
  user = (
      db.query(User)
      .filter(User.username == username, User.password == password)
      .first()
  )
  db.close()
  return user


def show_all_shoes():
  db = SessionLocal()
  shoes = db.query(Shoe).order_by(Shoe.size).all()
  for s in shoes:
    print("Size:", s.size, "| Brand:", s.brand, "| Price:", s.price, "| Pairs:", s.stock)
  db.close()


def add_pairs(size, pairs, staff_name):
  db = SessionLocal()
  shoe = db.query(Shoe).filter(Shoe.size == size).first()
  if shoe:
    shoe.stock = shoe.stock + pairs
    log = StockLog(
        shoe_id=shoe.id,
        staff_name=staff_name,
        added_pairs=pairs,
        new_stock=shoe.stock,
    )
    db.add(log)
    db.commit()
    print("Stock add ho gaya! New stock:", shoe.stock)
  else:
    print("Size nahi mila")
  db.close()


def show_stock_logs():
  db = SessionLocal()
  logs = db.query(StockLog).all()
  for log in logs:
    shoe = db.query(Shoe).filter(Shoe.id == log.shoe_id).first()
    size_no = shoe.size if shoe else log.shoe_id
    print(
        "Log ID:",
        log.id,
        "| Staff:",
        log.staff_name,
        "| Size:",
        size_no,
        "| Added:",
        log.added_pairs,
        "| New Stock:",
        log.new_stock,
    )
  db.close()


def buy_shoes(size, pairs, buyer_name):
  db = SessionLocal()
  shoe = db.query(Shoe).filter(Shoe.size == size).first()
  if shoe and shoe.stock >= pairs:
    shoe.stock = shoe.stock - pairs
    total = shoe.price * pairs
    sale = Sale(
        shoe_id=shoe.id,
        buyer_name=buyer_name,
        pairs=pairs,
        total_price=total,
    )
    db.add(sale)
    db.commit()
    print("Buy ho gaya! Total Bill:", total)
  else:
    print("Size nahi mila ya stock kam hai")
  db.close()


def update_price(size, new_price):
  db = SessionLocal()
  shoe = db.query(Shoe).filter(Shoe.size == size).first()
  if shoe:
    shoe.price = new_price
    db.commit()
    print("Price update ho gayi:", new_price)
  else:
    print("Size nahi mila")
  db.close()


def delete_shoe_size(size):
  db = SessionLocal()
  shoe = db.query(Shoe).filter(Shoe.size == size).first()
  if shoe:
    db.delete(shoe)
    db.commit()
    print("Size delete ho gaya")
  else:
    print("Size nahi mila")
  db.close()


def show_sales():
  db = SessionLocal()
  sales = db.query(Sale).all()
  for sale in sales:
    print("Sale ID:", sale.id, "| Buyer:", sale.buyer_name, "| Pairs:", sale.pairs, "| Total:", sale.total_price)
  db.close()


def create_user(username, password, role):
  db = SessionLocal()
  existing = db.query(User).filter(User.username == username).first()
  if not existing:
    db.add(User(username=username, password=password, role=role))
    db.commit()
    print("User ban gaya:", username)
  else:
    print("Username pehle se mojood hai")
  db.close()