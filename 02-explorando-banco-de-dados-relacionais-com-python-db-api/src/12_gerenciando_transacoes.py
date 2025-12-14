import sqlite3

from pathlib import Path


ROOT_PATH = Path(__file__).parent


def create_conn():
    conn = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
    return conn


def gerenciando_transacoes(conn):  
    # definição de sql's  
    sql_create = """
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero INTEGER,
        cliente VARCHAR(50),
        saldo REAL)
    """
    sql_insert = "INSERT INTO contas (numero, cliente, saldo) VALUES (?,?,?)"
    sql_update = "UPDATE contas SET numero=?, cliente=?, saldo=? WHERE id=?"
    sql_select = "SELECT id, numero, cliente, saldo FROM contas"
    
    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # criação da tabela
        cursor.execute(sql_create)

        # agrupando transações de inserção
        data = [
            (1, "Cliente1", 1000.0),
            (2, "Cliente1", 1000.0)        
        ]    
        cursor.executemany(sql_insert, data)
        conn.commit()

        # consultando os valores atuais   
        cursor.execute(sql_select)
        result1 = cursor.fetchall()

        # exibindo os resultados
        for row in result1:
            print(f"{row['id']}, {row['numero']}, {row['cliente']}, "
                  f"{row['saldo']}")        

        # agrupando transações de update
        # transferindo 100.0 da conta 1 para a conta 2.
        # agrupando transações, ou seja, um commit para as duas.
        # caso ocorra algo errado, nhm das operações serão realizadas.
        data1 = (1, "Cliente1", 900.0, 1)
        data2 = (2, "Cliente2", 1100.0, 2)

        print("Transferindo valores...")
        cursor.execute(sql_update, data1)
        cursor.execute(sql_update, data2)
        conn.commit()

        # consultando os valores atuais
        cursor.execute(sql_select)   
        result2 = cursor.fetchall()

        # exibindo os resultados
        for row in result2:
            print(f"{row['id']}, {row['numero']}, {row['cliente']}, "
                  f"{row['saldo']}")   
    except Exception as e:
        print(f"Falha ao realizar operações no banco: {e}.")
        conn.rollback()
    finally:
        conn.close()


def main():
    conn = create_conn()
    gerenciando_transacoes(conn)


if __name__ == "__main__":
    main()

