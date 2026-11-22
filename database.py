import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

password = os.getenv("DB_PASSWORD")
url = f"postgresql+psycopg2://postgres:{password}@localhost/shoes_shop"

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()