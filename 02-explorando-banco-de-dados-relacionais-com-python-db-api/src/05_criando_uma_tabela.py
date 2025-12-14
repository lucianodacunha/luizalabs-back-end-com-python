import sqlite3

from pathlib import Path


ROOT_PATH = Path(__file__).parent
conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(150)
    )""")
