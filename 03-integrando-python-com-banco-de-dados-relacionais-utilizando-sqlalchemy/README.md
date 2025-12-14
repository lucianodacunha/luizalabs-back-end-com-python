# Integrando Python com Banco de Dados Relacionais Utilizando SQLAlchemy

## Apresentação 

**integrar Python e bancos de dados relacionais de forma produtiva, segura e sustentável**, usando SQLAlchemy como camada de abstração.

Passando por tópicos como:

* a modelar dados com objetos Python;
* a persistir e consultar dados sem escrever SQL manual o tempo todo;
* a entender o que o ORM faz *por baixo do capô*.

O foco não é “esconder o banco”, mas **trabalhar em um nível mais alto sem perder controle**.

---

## Explorando a biblioteca SQLAlchemy

SQLAlchemy é uma biblioteca poderosa e modular. Ela tem dois grandes “lados”:

1. **Core**

   * camada de baixo nível;
   * trabalha com tabelas, colunas, SQL explícito;
   * próxima do DB-API.

2. **ORM**

   * camada de alto nível;
   * trabalha com classes, objetos e relacionamentos;
   * constrói SQL automaticamente.

O ORM usa o Core internamente.
Nada é feito “no escuro”.

---

## Entendendo o modelo ORM – Object Relational Mapping

ORM significa **Object Relational Mapping**.

A ideia é simples:

* uma tabela → uma classe Python;
* uma linha → uma instância da classe;
* uma coluna → um atributo do objeto.

Exemplo mental:

Tabela `usuarios`
→ Classe `Usuario`

Linha:

```
id=1, nome="Luciano"
```

vira:

```python
usuario = Usuario(id=1, nome="Luciano")
```

O ORM cuida de:

* transformar objetos em SQL (`INSERT`, `UPDATE`);
* transformar resultados de `SELECT` em objetos;
* sincronizar estado entre memória e banco.

---

## Considerações sobre o uso de ORM

ORM **não é sempre obrigatório**.

Vantagens:

* produtividade;
* menos SQL repetitivo;
* código mais expressivo;
* integração natural com frameworks (FastAPI, por exemplo).

Cuidados:

* abstração demais pode esconder consultas ineficientes;
* joins mal pensados podem virar problemas de performance;
* nem tudo precisa (ou deve) ser ORM.

Regra prática saudável:

* use ORM para CRUD e lógica de domínio;
* use SQL explícito para consultas críticas ou muito específicas.

---

## Primeiro contato com PyCharm IDE

PyCharm é uma IDE muito usada no ecossistema Python, especialmente com ORM, porque:

* entende bem type hints;
* autocompleta modelos ORM;
* navega facilmente entre entidades e consultas;
* ajuda no refactoring.

Não é obrigatório, mas ajuda bastante quando o projeto cresce.

---

## Instalando a biblioteca SQLAlchemy e considerações sobre a IDE

Com Poetry (alinhado ao que você já vem usando):

```bash
poetry add sqlalchemy
```

Para SQLite, não é necessário driver extra — ele já vem no Python.

Se for usar PostgreSQL ou SQL Server depois:

* PostgreSQL → `psycopg`
* SQL Server → `pyodbc`

A IDE deve estar usando o **mesmo ambiente virtual** criado pelo Poetry.

---

## Modelagem de dados do banco (cenário simplificado)

Vamos assumir um cenário simples:

* Usuários
* Pedidos

Relacionamento:

* um usuário pode ter vários pedidos;
* um pedido pertence a um usuário.

Conceitualmente:

* `usuarios (1) → (N) pedidos`

Isso já é suficiente para explorar praticamente todo o ORM.

---

## Criando as entidades com `declarative_base` – Parte 1

O ponto de partida do ORM é a base declarativa.

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

Agora criamos uma entidade:

```python
from sqlalchemy import Column, Integer, String, Boolean

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    ativo = Column(Boolean, default=True)
```

Aqui:

* `Usuario` é uma classe Python normal;
* `__tablename__` define a tabela;
* cada `Column` mapeia uma coluna SQL.

---

## Criando as entidades com `declarative_base` – Parte 2

Agora o segundo lado do domínio: pedidos.

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
```

Aqui já aparece o conceito de **chave estrangeira** no ORM.

---

## Definindo os relacionamentos e método de representação

Agora ligamos as entidades:

```python
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    ativo = Column(Boolean, default=True)

    pedidos = relationship("Pedido", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario id={self.id} nome={self.nome}>"
```

E no outro lado:

```python
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    total = Column(Integer, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="pedidos")

    def __repr__(self):
        return f"<Pedido id={self.id} total={self.total}>"
```

Agora:

* `usuario.pedidos` funciona;
* `pedido.usuario` funciona;
* o ORM sabe como montar os joins.

---

## Considerações sobre o código

Boas práticas nesse ponto:

* nomes claros para entidades;
* evitar lógica pesada dentro dos modelos;
* usar `__repr__` para debug, não para lógica de negócio;
* manter modelos próximos da estrutura do banco.

O ORM não substitui design — ele **exige** design.

---

## Conectando ao SQLite utilizando Engines e inspecionando o SQLite

A conexão começa com o **Engine**:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///exemplo.db", echo=True)
```

* `sqlite:///exemplo.db` → caminho do banco;
* `echo=True` → mostra o SQL gerado (excelente para aprendizado).

Você pode inspecionar o banco:

```python
from sqlalchemy import inspect

insp = inspect(engine)
print(insp.get_table_names())
```

Isso mostra as tabelas existentes.

---

## Criando uma sessão para persistir dados no SQLite

A sessão é a ponte entre objetos e banco.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

Agora você pode persistir objetos:

```python
usuario = Usuario(nome="Luciano", email="luciano@email.com")
session.add(usuario)
session.commit()
```

A sessão:

* acompanha mudanças nos objetos;
* decide quando gerar SQL;
* controla transações.

---

## Executando consultas ao BD – SQLAlchemy ORM

Consulta básica:

```python
usuarios = session.query(Usuario).all()
```

Filtro:

```python
usuario = session.query(Usuario).filter_by(email="luciano@email.com").first()
```

Filtro mais expressivo:

```python
usuarios_ativos = session.query(Usuario).filter(Usuario.ativo == True).all()
```

Tudo isso vira SQL real, executado no banco.

---

## Consultas com ORDER BY, JOIN e COUNT

Order:

```python
session.query(Usuario).order_by(Usuario.nome).all()
```

Join:

```python
session.query(Pedido).join(Pedido.usuario).filter(Usuario.nome == "Luciano").all()
```

Count:

```python
from sqlalchemy import func

total_usuarios = session.query(func.count(Usuario.id)).scalar()
```

Aqui você começa a ver o ORM como **construtor de consultas**, não só CRUD.

---

## Criando esquema com SQLAlchemy Metadata

A `Base` mantém um objeto `metadata` com todas as tabelas mapeadas.

```python
Base.metadata.tables
```

Esse metadata representa o esquema inteiro em memória.

---

## Submetendo a estrutura criada ao SQLite e executando SQL Statements

Criar as tabelas no banco:

```python
Base.metadata.create_all(engine)
```

Isso:

* cria apenas tabelas que não existem;
* respeita a definição das entidades.

Você ainda pode executar SQL puro quando quiser:

```python
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios"))
    print(result.fetchall())
```

ORM e SQL convivem muito bem no SQLAlchemy.

---

## Fechando o ciclo

Ao final desse módulo, você entende que:

* SQLAlchemy **não elimina SQL**, ele o organiza;
* o ORM é um mapeamento consciente, não uma abstração cega;
* engines, sessões e metadata são peças claras, não mágicas.

Isso prepara o terreno perfeito para:

* integração com FastAPI;
* uso de sessões por request;
* migrations;
* consultas mais complexas sem perder sanidade.

Aqui você não está “aprendendo ORM”.
Está aprendendo a **modelar domínio e persistência com maturidade técnica** — e isso é um superpoder silencioso no backend moderno.
