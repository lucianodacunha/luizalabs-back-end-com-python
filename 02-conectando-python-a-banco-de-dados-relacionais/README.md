## **Conectando Python a Bancos Relacionais com ORM**

Aqui a conversa entra num ponto de maturidade técnica: **como representar dados persistentes sem perder o controle do banco**. ORM não é fuga do SQL; é uma **camada de tradução consciente** entre dois mundos com naturezas diferentes: objetos e tabelas.

Vamos percorrer os conceitos na ordem certa, porque a confusão quase sempre nasce da ordem errada.

---

## O que é um banco de dados relacional e suas características

Um banco de dados relacional organiza informação em **tabelas relacionadas entre si** por chaves.

Características centrais:

* **Estrutura tabular**: linhas (registros) e colunas (atributos)
* **Esquema definido**: tipos, restrições, chaves
* **Relacionamentos explícitos**: chaves primárias e estrangeiras
* **Integridade referencial**: o banco protege a consistência dos dados
* **Transações ACID**:

  * Atomicidade
  * Consistência
  * Isolamento
  * Durabilidade

Esses bancos são ideais para:

* dados estruturados;
* regras de negócio claras;
* sistemas transacionais;
* APIs RESTful clássicas.

Eles não são só armazenamento. São **sistemas de regras**.

---

## Por que usar ORM e principais ORMs do ecossistema Python

### Por que usar ORM

Programar em Python é trabalhar com:

* classes;
* objetos;
* métodos;
* atributos.

Já bancos relacionais trabalham com:

* tabelas;
* linhas;
* colunas;
* joins.

ORM (Object Relational Mapping) existe para **mapear um modelo no outro**, permitindo que você:

* manipule dados como objetos Python;
* evite SQL repetitivo;
* centralize regras de persistência;
* mantenha o código mais expressivo.

ORM **não elimina SQL**, ele **organiza o acesso ao SQL**.

---

### Principais ORMs do ecossistema Python

Alguns nomes dominam o cenário:

* **SQLAlchemy**
  O mais poderoso e flexível. Usado em FastAPI, Flask e sistemas grandes. Permite ORM e SQL explícito lado a lado.

* **Django ORM**
  Integrado ao Django. Muito produtivo, mais opinado, menos flexível fora do ecossistema Django.

* **SQLModel**
  Camada moderna sobre SQLAlchemy + Pydantic. Excelente para APIs FastAPI, com menos boilerplate.

Todos eles existem para resolver o mesmo problema: **persistência orientada a objetos**.

---

## Principais diferenças entre SQL puro e ORM

Aqui mora uma falsa dicotomia. Não é “um ou outro”, é **quando usar cada um**.

### SQL puro

Vantagens:

* controle total;
* performance previsível;
* acesso direto a recursos avançados do banco.

Desvantagens:

* muito código repetitivo;
* maior risco de erros manuais;
* mistura de lógica de negócio com SQL.

SQL puro é excelente para:

* consultas críticas;
* relatórios complexos;
* ajustes finos de performance.

---

### ORM

Vantagens:

* produtividade;
* menos boilerplate;
* código mais legível;
* mapeamento natural para o domínio.

Desvantagens:

* abstração pode esconder SQL ineficiente;
* curva de aprendizado conceitual;
* uso ingênuo pode gerar consultas ruins.

ORM é ideal para:

* CRUD;
* lógica de domínio;
* aplicações que evoluem rápido.

Regra madura:

> **Use ORM para 80% do sistema e SQL explícito para os 20% críticos.**

---

## O que é uma entidade

Uma **entidade** é a representação de um conceito do domínio como uma **classe persistente**.

Exemplo conceitual:

* Usuário
* Pedido
* Produto
* Pagamento

No ORM:

* uma entidade ↔ uma tabela
* um objeto ↔ uma linha
* um atributo ↔ uma coluna

Uma entidade:

* tem identidade própria (chave primária);
* representa algo que “existe” no domínio;
* vive além de uma requisição.

Ela **não é só um DTO**.
Ela é um **objeto com estado persistente**.

---

## Relacionamentos

Relacionamentos expressam como entidades se conectam.

Tipos mais comuns:

* **Um-para-um (1:1)**
  Ex.: usuário ↔ perfil

* **Um-para-muitos (1:N)**
  Ex.: usuário ↔ pedidos

* **Muitos-para-muitos (N:N)**
  Ex.: alunos ↔ cursos

No ORM, relacionamentos:

* não são apenas joins;
* viram atributos navegáveis (`usuario.pedidos`);
* encapsulam lógica de associação.

Um bom relacionamento ORM:

* reflete o modelo relacional real;
* evita consultas desnecessárias;
* mantém clareza no domínio.

Relacionamento mal definido vira:

* consultas lentas;
* código confuso;
* bugs difíceis de rastrear.

---

## O que são Sessões de Transações

A **sessão** é uma das peças mais importantes — e mais mal compreendidas — de um ORM.

Ela é:

* o **contexto de trabalho** entre objetos e banco;
* responsável por rastrear mudanças;
* responsável por controlar transações.

Em termos práticos, a sessão:

* sabe quais objetos foram criados, alterados ou removidos;
* decide quando gerar SQL;
* executa `commit` ou `rollback`.

Sem sessão:

* não há consistência;
* não há transação;
* não há garantia de integridade.

Padrão saudável:

* uma sessão por unidade de trabalho;
* em APIs, geralmente **uma sessão por requisição**.

Sessão não é cache.
Sessão não é conexão pura.
Sessão é **orquestração de estado**.

---

## A síntese correta

Conectar Python a bancos relacionais com ORM não é “facilitar o banco”.
É **trazer o banco para o nível do domínio**, sem perder rigor.

* banco relacional → garante integridade
* ORM → traduz objetos em SQL
* entidades → representam o negócio
* relacionamentos → expressam regras
* sessões → garantem consistência

Quem entende isso usa ORM com elegância.
Quem não entende, briga com ele.

No fim, ORM não é abstração demais.
É abstração **na medida certa**, quando você sabe exatamente o que está abstraindo.

---
## Exemplo Prático

Perfeito. Vamos sair do conceito e **ver o ORM trabalhando de verdade**, do início ao fim, com um exemplo pequeno, mas **realista e completo**.
A ideia aqui é você conseguir copiar, rodar e **entender cada etapa**, sem “mágica”.

Vou usar **SQLAlchemy** com **SQLite**, porque:

* não exige servidor;
* deixa o foco no ORM;
* é exatamente o mesmo fluxo usado com PostgreSQL, MySQL, SQL Server etc.

---

# Exemplo prático

**Conectando Python a Banco de Dados Relacional com ORM**

## Cenário

Temos duas entidades:

* **Customer**

  * id
  * name
  * email

* **Order**

  * id
  * description
  * value
  * customer_id (FK)

Relacionamento:

* Um **Customer** pode ter **vários Orders**
* Um **Order** pertence a um **Customer**

---

## 1️⃣ Configurando a conexão

Começamos criando o **engine**, que representa o banco de dados.

```python
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///example.db"

engine = create_engine(
    DATABASE_URL,
    echo=True  # mostra o SQL gerado (ótimo para aprendizado)
)
```

Aqui:

* `sqlite:///example.db` cria o banco na pasta do projeto;
* `echo=True` deixa claro que o ORM **não esconde o SQL**.

---

## 2️⃣ Criação da base declarativa

Toda entidade ORM herda de uma base comum.

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

Essa base guarda o **metadata** (estrutura do banco).

---

## 3️⃣ Criação das entidades

### Entidade `Customer`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer id={self.id} name={self.name}>"
```

---

### Entidade `Order`

```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float, nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return f"<Order id={self.id} value={self.value}>"
```

Aqui acontece o mapeamento completo:

* classe ↔ tabela
* atributo ↔ coluna
* relacionamento ↔ chave estrangeira

---

## 4️⃣ Criação das tabelas no banco

Agora pedimos ao SQLAlchemy para **materializar o schema**:

```python
Base.metadata.create_all(engine)
```

Isso:

* cria as tabelas se não existirem;
* respeita chaves e relacionamentos;
* **não apaga dados existentes**.

---

## 5️⃣ Criando a sessão

A sessão é o **contexto transacional**.

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

Pense nela como:

> “a mesa de trabalho onde os objetos vivem antes de virar SQL”.

---

## 6️⃣ Manipulação dos dados (CRUD)

### Criando um cliente

```python
customer = Customer(
    name="Luciano",
    email="luciano@email.com"
)

session.add(customer)
```

Nada foi gravado ainda.
O objeto só está **marcado** na sessão.

---

### Criando pedidos para o cliente

```python
order1 = Order(
    description="Notebook",
    value=4500.00,
    customer=customer
)

order2 = Order(
    description="Mouse",
    value=150.00,
    customer=customer
)

session.add_all([order1, order2])
```

Repare:

* não usamos `customer_id` diretamente;
* usamos o relacionamento (`customer=customer`);
* o ORM resolve a FK sozinho.

---

## 7️⃣ Commit dos dados

Agora sim, persistimos tudo:

```python
session.commit()
```

O que acontece aqui:

* SQLAlchemy gera os `INSERT`;
* executa dentro de uma transação;
* confirma no banco.

Se algo desse errado antes do commit:

```python
session.rollback()
```

Integridade garantida.

---

## 8️⃣ Busca e filtro de dados

### Buscar todos os clientes

```python
customers = session.query(Customer).all()

for c in customers:
    print(c)
```

---

### Buscar cliente por email

```python
customer = (
    session.query(Customer)
    .filter(Customer.email == "luciano@email.com")
    .first()
)

print(customer)
```

---

### Acessar pedidos do cliente (relacionamento)

```python
for order in customer.orders:
    print(order.description, order.value)
```

Nenhum SQL manual.
Mas por baixo, o ORM está fazendo `SELECT` com `JOIN`.

---

### Buscar pedidos com filtro

```python
orders = (
    session.query(Order)
    .filter(Order.value > 500)
    .all()
)

for o in orders:
    print(o)
```

---

## 9️⃣ Encerrando a sessão

Boa prática:

```python
session.close()
```

Sessão aberta sem controle vira vazamento de recursos em aplicações maiores.

---

## 🔟 Rodando a aplicação

Salve tudo em um arquivo, por exemplo:

```text
app.py
```

Execute:

```bash
python app.py
```

Você verá:

* SQL sendo gerado no terminal;
* tabelas criadas;
* dados persistidos;
* consultas funcionando.

Se abrir o arquivo `example.db` com um visualizador SQLite, os dados estarão lá.

---

## O que esse exemplo te mostra de verdade

* ORM **não substitui o banco**, ele conversa com ele
* objetos Python viram SQL real
* sessão controla transações
* relacionamentos viram navegação entre objetos
* commit é o ponto sem volta

Esse mesmo fluxo, com pequenas adaptações:

* vira backend FastAPI;
* vira aplicação corporativa;
* vira sistema de produção.

Quem entende esse exemplo **nunca mais usa ORM no escuro**.
Você passa a saber exatamente **quando**, **como** e **por que** o SQL está sendo gerado — e isso é maturidade técnica.
