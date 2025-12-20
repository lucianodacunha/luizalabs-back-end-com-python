# Manipulação de Dados com FastAPI Assíncrono

## Conexão com o banco de dados assíncrono

### Por que banco assíncrono importa?

FastAPI é assíncrono por natureza.
Se você usa banco **síncrono** dentro de `async def`, você bloqueia o event loop — ou seja, perde o principal benefício do framework.

Para usar banco de forma assíncrona, você precisa de:

* **driver async**
* **engine async**
* **session async**

No ecossistema SQLAlchemy moderno, isso é feito com:

* `sqlalchemy.ext.asyncio`
* drivers como `aiosqlite`, `asyncpg`, etc.

---

### Criando o engine assíncrono (SQLite como exemplo)

```python
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./database/app.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)
```

Pontos importantes:

* `sqlite+aiosqlite` → dialeto async
* `echo=True` → mostra o SQL (ótimo para aprendizado)
* a URL muda **só no prefixo**, o conceito é o mesmo

---

### Criando a sessão assíncrona

```python
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
```

E uma função para obter a sessão (padrão FastAPI):

```python
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
```

Isso garante:

* uma sessão por request;
* fechamento automático;
* transações bem delimitadas.

---

## Modelos de dados com FastAPI

Aqui entram **dois tipos de modelos**, com responsabilidades diferentes:

1. **Modelos ORM (SQLAlchemy)** → persistência
2. **Modelos Pydantic (FastAPI)** → entrada e saída de dados

Misturar os dois é erro conceitual comum.

---

### Modelo ORM (SQLAlchemy)

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```

Esse modelo:

* sabe falar com o banco;
* não sabe nada sobre HTTP.

---

### Modelos Pydantic (FastAPI)

```python
from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True
```

Aqui:

* `UsuarioCreate` → entrada (POST / PUT)
* `UsuarioResponse` → saída (JSON)
* `orm_mode = True` permite converter objetos ORM em JSON automaticamente

Separação de responsabilidades = código saudável.

---

## Operações CRUD assíncronas em APIs RESTful

Agora o coração do sistema: **CRUD assíncrono**, alinhado a REST.

---

### CREATE – Criar recurso

```python
from sqlalchemy.ext.asyncio import AsyncSession

async def criar_usuario(
    session: AsyncSession,
    usuario_data: UsuarioCreate
):
    usuario = Usuario(**usuario_data.dict())
    session.add(usuario)
    await session.commit()
    await session.refresh(usuario)
    return usuario
```

O que acontece aqui:

* `session.add()` → marca para inserção
* `commit()` → grava no banco
* `refresh()` → carrega campos gerados (ex: id)

---

### READ – Consultar recursos

Buscar todos:

```python
from sqlalchemy import select

async def listar_usuarios(session: AsyncSession):
    result = await session.execute(select(Usuario))
    return result.scalars().all()
```

Buscar por ID:

```python
async def obter_usuario(session: AsyncSession, usuario_id: int):
    result = await session.execute(
        select(Usuario).where(Usuario.id == usuario_id)
    )
    return result.scalar_one_or_none()
```

Note:

* `select()` vem do SQLAlchemy Core
* `.scalars()` extrai os objetos ORM
* tudo é `await`

---

### UPDATE – Atualizar recurso

```python
async def atualizar_usuario(
    session: AsyncSession,
    usuario: Usuario,
    dados: UsuarioCreate
):
    for campo, valor in dados.dict().items():
        setattr(usuario, campo, valor)

    await session.commit()
    await session.refresh(usuario)
    return usuario
```

Aqui:

* você altera o objeto em memória;
* o ORM detecta mudanças;
* o SQL é gerado automaticamente.

---

### DELETE – Remover recurso

```python
async def remover_usuario(
    session: AsyncSession,
    usuario: Usuario
):
    await session.delete(usuario)
    await session.commit()
```

Sem SQL manual, mas com transação real por baixo.

---

## Implementação final do CRUD (FastAPI)

Agora juntamos tudo em endpoints RESTful.

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()
```

---

### CREATE – POST

```python
@app.post("/usuarios", response_model=UsuarioResponse)
async def criar(
    usuario: UsuarioCreate,
    session: AsyncSession = Depends(get_session)
):
    return await criar_usuario(session, usuario)
```

---

### READ – GET

```python
@app.get("/usuarios", response_model=list[UsuarioResponse])
async def listar(
    session: AsyncSession = Depends(get_session)
):
    return await listar_usuarios(session)
```

```python
@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
async def obter(
    usuario_id: int,
    session: AsyncSession = Depends(get_session)
):
    usuario = await obter_usuario(session, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario
```

---

### UPDATE – PUT / PATCH

```python
@app.put("/usuarios/{usuario_id}", response_model=UsuarioResponse)
async def atualizar(
    usuario_id: int,
    dados: UsuarioCreate,
    session: AsyncSession = Depends(get_session)
):
    usuario = await obter_usuario(session, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404)

    return await atualizar_usuario(session, usuario, dados)
```

---

### DELETE – DELETE

```python
@app.delete("/usuarios/{usuario_id}", status_code=204)
async def remover(
    usuario_id: int,
    session: AsyncSession = Depends(get_session)
):
    usuario = await obter_usuario(session, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404)

    await remover_usuario(session, usuario)
```

---

## O quadro geral (o que realmente importa)

Esse modelo de integração garante:

* FastAPI continua **não bloqueante**
* banco de dados é acessado de forma **assíncrona real**
* ORM cuida da persistência, não da arquitetura
* Pydantic garante contratos claros
* CRUD segue REST de forma previsível

O mais importante:
você passa a enxergar a API como **orquestradora de estados**, não como um monte de endpoints soltos.

Daqui pra frente, os próximos degraus naturais são:

* paginação e filtros;
* autenticação;
* migrations;
* testes assíncronos;
* performance e pool de conexões.

Mas a base está sólida.
Aqui você já está escrevendo **backend moderno de verdade**, não tutorial descartável.
