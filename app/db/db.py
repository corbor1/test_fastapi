from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

URL = "postgresql+psycopg2://postgres:mysecretpassword@127.0.0.1:5433/mydb"

engine = create_engine(URL)
SessionLocal = sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine)

Base = DeclarativeBase()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()