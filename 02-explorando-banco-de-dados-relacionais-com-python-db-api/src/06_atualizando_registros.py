import sqlite3

from pathlib import Path


ROOT_PATH = Path(__file__).parent


def create_conn():
    conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
    return conn


def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(150)
    )
    """)


def insert(conn):
    cursor = conn.cursor()
    data = ("Luciano", "luciano@email.com")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conn.commit()


def update(conn):
    data = ("Luciano Cunha", "luciano@email.com.br", 1)
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes set nome=?, email=? WHERE id=?", data)
    conn.commit()


def main():
    conn = create_conn()
    update(conn)


if __name__ == "__main__":
    main()

