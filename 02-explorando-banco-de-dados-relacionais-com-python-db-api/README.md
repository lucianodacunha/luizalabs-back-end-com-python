Perfeito. Aqui a gente sai do “banco como conceito” e entra no **banco como código executando de verdade**.
O Python DB-API é aquele nível fundamental: não é ORM, não é abstração mágica — é o chão da fábrica. Quem entende isso, nunca mais fica refém de framework.

Vou tratar as três “partes” como uma progressão de entendimento, e depois entrar no uso prático com Python.

---

## Introdução aos Bancos de Dados Relacionais – Parte 1

**O modelo mental**

Bancos relacionais organizam dados em:

* tabelas;
* linhas;
* colunas;
* relações bem definidas.

A ideia central é **normalização**: evitar duplicação e inconsistência.
Você não grava “o mesmo dado em vários lugares”; você referencia.

Exemplo clássico:

* tabela `usuarios`
* tabela `pedidos`
* `pedidos.usuario_id` aponta para `usuarios.id`

Isso permite:

* integridade dos dados;
* consultas poderosas;
* regras claras de negócio.

Essa parte é sobre **estrutura e relacionamento**, não sobre código ainda.

---

## Introdução aos Bancos de Dados Relacionais – Parte 2

**SQL como linguagem declarativa**

SQL não diz *como* buscar os dados, mas *o que* você quer.

Exemplo mental:

* “Quero todos os usuários ativos”
* “Quero pedidos do usuário 10”
* “Quero a soma de vendas por mês”

Você declara a intenção, o DBMS decide o plano de execução.

Conceitos-chave:

* `SELECT` → leitura
* `INSERT` → criação
* `UPDATE` → alteração
* `DELETE` → remoção
* `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`

SQL é padrão, mas cada banco tem seus dialetos.
O Python DB-API abstrai a **conexão**, não o SQL.

---

## Introdução aos Bancos de Dados Relacionais – Parte 3

**Concorrência, integridade e transações**

Aqui entra o “modo adulto” do banco.

* várias conexões ao mesmo tempo;
* vários usuários alterando dados;
* necessidade de consistência.

É por isso que existem:

* **transações**;
* **locks**;
* **isolamento**;
* **commit** e **rollback**.

Sem isso, APIs quebram silenciosamente.

Essa parte conecta diretamente com boas práticas que veremos mais adiante.

---

## Python DB-API (PEP 249) – visão geral

A **Python DB-API** é um padrão (PEP 249) que define:

* como conectar;
* como executar comandos SQL;
* como recuperar resultados.

Drivers diferentes seguem a mesma ideia:

* `sqlite3` (nativo)
* `psycopg2` / `psycopg` (PostgreSQL)
* `pyodbc` (SQL Server, vários outros)
* `mysql-connector-python`

Os nomes mudam pouco, o conceito é o mesmo.

---

## Conectando com o banco de dados

Exemplo usando `sqlite3` (ideal para estudo, zero setup):

```python
import sqlite3

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
```

O que temos aqui:

* `conn` → conexão com o banco
* `cursor` → objeto que executa SQL e lê resultados

Em bancos maiores (Postgres, SQL Server), a ideia é idêntica, só muda o driver.

---

## Criando uma tabela

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    ativo BOOLEAN NOT NULL
)
""")

conn.commit()
```

Pontos importantes:

* `execute()` envia SQL ao banco;
* `commit()` confirma a transação;
* sem `commit()`, a tabela pode nem existir de verdade.

---

## Inserindo registros

```python
cursor.execute(
    "INSERT INTO usuarios (nome, email, ativo) VALUES (?, ?, ?)",
    ("Luciano", "luciano@email.com", True)
)

conn.commit()
```

Nunca concatene SQL com string manualmente.
Os `?` (ou `%s`, dependendo do driver) protegem contra SQL Injection.

---

## Atualizando registros

```python
cursor.execute(
    "UPDATE usuarios SET ativo = ? WHERE email = ?",
    (False, "luciano@email.com")
)

conn.commit()
```

Sempre use `WHERE`.
Update sem `WHERE` é a versão digital de “apagar o banco sem backup”.

---

## Removendo registros

```python
cursor.execute(
    "DELETE FROM usuarios WHERE id = ?",
    (1,)
)

conn.commit()
```

Mesma regra: `DELETE` sem `WHERE` remove tudo.

---

## Inserindo registros em lote

Para volume maior de dados, use `executemany()`:

```python
usuarios = [
    ("Maria", "maria@email.com", True),
    ("João", "joao@email.com", False),
    ("Ana", "ana@email.com", True),
]

cursor.executemany(
    "INSERT INTO usuarios (nome, email, ativo) VALUES (?, ?, ?)",
    usuarios
)

conn.commit()
```

Isso:

* reduz overhead;
* melhora performance;
* mantém código limpo.

---

## Consultando os registros

```python
cursor.execute("SELECT id, nome, email, ativo FROM usuarios")

rows = cursor.fetchall()

for row in rows:
    print(row)
```

Por padrão, cada `row` é uma tupla:

```python
(1, "Luciano", "luciano@email.com", 1)
```

Você pode usar:

* `fetchone()`
* `fetchmany(n)`
* `fetchall()`

---

## Alterando o `row_factory`

Para deixar os resultados mais amigáveis, você pode mudar o formato das linhas.

Exemplo com `sqlite3.Row`:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

for row in rows:
    print(row["nome"], row["email"])
```

Agora cada linha se comporta como um dicionário.

Em outros drivers:

* PostgreSQL → `RealDictCursor`
* SQL Server → abordagens semelhantes via driver

Isso é muito útil para APIs que retornam JSON.

---

## Boas práticas

Algumas regras que salvam projetos:

* sempre use parâmetros (nunca SQL concatenado);
* feche conexões (`conn.close()`);
* evite conexões globais sem controle;
* agrupe operações relacionadas em transações;
* trate exceções do banco explicitamente;
* logue erros, mas não exponha SQL ao cliente.

No contexto de FastAPI, conexões geralmente ficam:

* por request;
* ou gerenciadas por pool.

### Sempre use parâmetros (nunca SQL concatenado)

### O problema

Concatenar SQL com strings vindas do usuário é uma porta escancarada para **SQL Injection**.

Exemplo perigoso:

```python
email = input("Email: ")
cursor.execute(
    f"SELECT * FROM usuarios WHERE email = '{email}'"
)
```

Se alguém passar:

```text
' OR 1=1 --
```

O SQL vira:

```sql
SELECT * FROM usuarios WHERE email = '' OR 1=1 --
```

Resultado: retorna **todos os usuários**. Em casos piores, apaga tabelas.

---

### A forma correta

Use **parâmetros do driver**:

```python
cursor.execute(
    "SELECT * FROM usuarios WHERE email = ?",
    (email,)
)
```

Ou, dependendo do driver:

```python
cursor.execute(
    "SELECT * FROM usuarios WHERE email = %s",
    (email,)
)
```

Benefícios:

* proteção contra SQL Injection;
* melhor performance (query pode ser reutilizada);
* código mais legível.

Regra de ouro:
**se tem dado externo, tem parâmetro**. Sempre.

---

### Feche conexões (`conn.close()`)

### O problema

Cada conexão aberta:

* consome memória;
* ocupa recursos do DBMS;
* ocupa um “slot” de conexão.

Se você não fecha:

* o banco começa a recusar novas conexões;
* a API passa a falhar “do nada”.

Isso é clássico em sistemas que funcionam bem em dev e quebram em produção.

---

### A forma correta

Sempre feche explicitamente:

```python
conn = sqlite3.connect("exemplo.db")
try:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
finally:
    conn.close()
```

Ou melhor ainda, use **context manager** (quando o driver permite):

```python
with sqlite3.connect("exemplo.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
```

Ao sair do bloco:

* o commit/rollback acontece automaticamente;
* a conexão é fechada.

No contexto de APIs, isso evita vazamento silencioso de conexões.

---

### Evite conexões globais sem controle

### O problema

Algo assim parece conveniente:

```python
conn = sqlite3.connect("exemplo.db")

def listar_usuarios():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()
```

Mas isso é perigoso porque:

* conexões **não são thread-safe** na maioria dos drivers;
* em APIs, múltiplas requisições usam o mesmo objeto ao mesmo tempo;
* você cria condições de corrida, deadlocks e corrupção de estado.

Em FastAPI, isso fica ainda mais crítico por causa de concorrência.

---

### A forma correta

Padrão saudável:

* uma conexão por unidade de trabalho;
* ou uso de **pool de conexões**.

Exemplo simples:

```python
def get_connection():
    return sqlite3.connect("exemplo.db")

def listar_usuarios():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()
    finally:
        conn.close()
```

Em frameworks modernos:

* o pool gerencia abertura/fechamento;
* você pega e devolve conexões como se fossem recursos finitos.

Conexão global sem controle é dívida técnica com juros altos.

---

### Agrupe operações relacionadas em transações

### O problema

Imagine duas operações que **dependem uma da outra**:

1. criar usuário
2. criar pedido para esse usuário

Sem transação:

```python
cursor.execute("INSERT INTO usuarios ...")
cursor.execute("INSERT INTO pedidos ...")
conn.commit()
```

Se a segunda falhar:

* o usuário fica criado;
* o pedido não existe;
* o sistema entra em estado inconsistente.

Isso é o famoso “meio gravado”.

---

### A forma correta

Use transações explicitamente:

```python
try:
    cursor.execute("INSERT INTO usuarios ...")
    cursor.execute("INSERT INTO pedidos ...")
    conn.commit()
except Exception:
    conn.rollback()
    raise
```

Aqui você garante:

* tudo acontece ou nada acontece;
* o banco mantém integridade.

Transação não é só detalhe técnico — é **regra de negócio** codificada.

---

### Trate exceções do banco explicitamente

### O problema

Capturar exceções de forma genérica:

```python
try:
    cursor.execute(...)
except Exception:
    pass
```

Isso:

* esconde erros reais;
* dificulta debug;
* faz o sistema “falhar silenciosamente”.

Ou pior: deixar exceções do banco vazarem direto para o cliente.

---

### A forma correta

Trate exceções de banco como eventos importantes:

```python
import sqlite3

try:
    cursor.execute(...)
    conn.commit()
except sqlite3.IntegrityError as e:
    conn.rollback()
    # tratar violação de chave única, por exemplo
    raise ValueError("Registro duplicado") from e
except sqlite3.DatabaseError as e:
    conn.rollback()
    # erro mais grave
    raise
```

Benefícios:

* você sabe **o que** falhou;
* pode mapear erros do banco para erros de negócio;
* evita comportamento imprevisível.

Em APIs, isso se conecta diretamente com **HTTP status codes** adequados.

---

### Logue erros, mas não exponha SQL ao cliente

### O problema

Retornar algo assim ao cliente:

```json
{
  "error": "SELECT * FROM usuarios WHERE senha = '123'"
}
```

Isso é:

* vazamento de informação sensível;
* convite para ataques;
* quebra de encapsulamento da aplicação.

Mas, ao mesmo tempo, **não logar nada** é igualmente ruim.

---

### A forma correta

Separar claramente:

* **o que vai para o log** (interno);
* **o que vai para o cliente** (externo).

Exemplo conceitual:

```python
import logging

logger = logging.getLogger(__name__)

try:
    cursor.execute(...)
except Exception as e:
    logger.exception("Erro ao acessar o banco de dados")
    raise RuntimeError("Erro interno ao processar a requisição")
```

No log (interno):

* stack trace;
* SQL;
* contexto técnico.

Para o cliente:

* mensagem genérica;
* sem detalhes internos.

Isso mantém:

* segurança;
* profissionalismo;
* capacidade real de manutenção.

---

## Gerenciando transações

Transações garantem que um conjunto de operações aconteça **por inteiro ou não aconteça**.

Exemplo clássico:

```python
try:
    cursor.execute(
        "INSERT INTO usuarios (nome, email, ativo) VALUES (?, ?, ?)",
        ("Carlos", "carlos@email.com", True)
    )

    cursor.execute(
        "INSERT INTO pedidos (usuario_id, total) VALUES (?, ?)",
        (cursor.lastrowid, 150.0)
    )

    conn.commit()

except Exception as e:
    conn.rollback()
    raise
```

Aqui:

* se qualquer comando falhar → `rollback()`;
* o banco volta ao estado anterior;
* a integridade é preservada.

Sem transações, dados ficam **meio gravados**, que é o pior estado possível.
