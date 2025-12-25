from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, event

from pathlib import Path


class Base(DeclarativeBase):
    pass

ROOT_PATH = Path(__file__).absolute().parent.parent
DB_PATH = ROOT_PATH / "app.db"

print(ROOT_PATH)
print(DB_PATH)

engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)

event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
