import time

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import get_settings

settings = get_settings()

DATABASE_URL = settings.DATABASE_URL

Base = declarative_base()

engine = None

for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("✅ Banco conectado!")
        break
    except Exception:
        print(f"⏳ Tentando conectar ao banco... ({i + 1}/10)")
        time.sleep(3)

if engine is None:
    raise Exception("❌ Não conseguiu conectar ao banco")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()