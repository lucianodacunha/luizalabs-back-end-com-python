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


def delete(conn):
    data = (1,)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conn.commit()


def insert_many(conn):
    cursor = conn.cursor()
    data = [
        ("Luciano", "luciano@email.com"),
        ("Python", "python@email.com"),
        ("VSCode", "vscode@email.com"),
    ]
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", data)
    conn.commit()


def select(conn):
    cursor = conn.cursor()
    id = (2,)
    cursor.execute("SELECT nome, email FROM clientes WHERE id=?", id)
    result = cursor.fetchone()
    print(result)


def select_all(conn):
    cursor = conn.cursor()
    id = (1,)
    cursor.execute("SELECT nome, email FROM clientes WHERE id > ?", id)
    result = cursor.fetchall()
    print(result)    


def row_factory(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    id = (1, )
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id > ?", id)
    result = cursor.fetchall()
    for client in result:
        print(client["id"], client["nome"], client["email"])


def main():
    conn = create_conn()
    row_factory(conn)


if __name__ == "__main__":
    main()

