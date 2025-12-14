import sqlite3

from pathlib import Path


ROOT_PATH = Path(__file__).parent
conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(150)
)
""")

data = ("Luciano", "luciano@email.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
conn.commit()
