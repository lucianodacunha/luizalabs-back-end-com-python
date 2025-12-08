# Primeiros Passos com FastAPI

## Criando uma aplicação FastAPI

O núcleo de tudo é o objeto `FastAPI`.
No arquivo `main.py`, algo assim:

```python
from fastapi import FastAPI

app = FastAPI(
    title="Minha API",
    version="1.0.0"
)
```

Esse `app` é a aplicação ASGI.
É ele que o Uvicorn vai usar:

```bash
uvicorn main:app --reload
```

* `main` → nome do módulo (arquivo `main.py`)
* `app` → objeto `FastAPI` lá dentro

---

## Estrutura básica de uma API FastAPI

A estrutura mínima de uma API é:

1. Criar a aplicação (`app = FastAPI()`).
2. Declarar rotas com decoradores (`@app.get`, `@app.post` etc.).
3. Rodar com Uvicorn.

Exemplo bem simples:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```

Coisas importantes aqui:

* As funções podem ser `async def` (recomendado na maioria dos casos).
* O retorno pode ser `dict`, `list`, modelos Pydantic etc. O FastAPI converte para JSON automaticamente.
* Documentação automática em:

  * `/docs` → Swagger UI
  * `/redoc` → ReDoc

---

## Rotas e endpoints em FastAPI – **Path parameters**

Path parameter é aquele pedaço da URL que faz parte do caminho, por exemplo:
`/usuarios/10` → o `10` é um path param.

No FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios/{usuario_id}")
async def obter_usuario(usuario_id: int):
    return {"usuario_id": usuario_id}
```

Alguns pontos:

* `{usuario_id}` na rota deve bater com o nome do parâmetro da função.
* O tipo (`int`) faz o FastAPI:

  * converter da string da URL para `int`;
  * validar (se vier “abc”, ele já responde 422).

Você ainda pode adicionar validações extras com `Path`, mas isso é um passo adiante:

```python
from fastapi import Path

@app.get("/usuarios/{usuario_id}")
async def obter_usuario(
    usuario_id: int = Path(gt=0, description="ID do usuário, maior que zero")
):
    return {"usuario_id": usuario_id}
```

---

## Rotas e endpoints em FastAPI – **Query parameters**

Query parameters são os que vêm depois do `?` na URL, ex:
`/usuarios?ativo=true&page=2&limit=10`.

No FastAPI, basta declarar parâmetros que **não estão** no path:

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/usuarios")
async def listar_usuarios(
    ativo: Optional[bool] = None,
    page: int = 1,
    limit: int = 10
):
    return {
        "filtros": {
            "ativo": ativo,
            "page": page,
            "limit": limit
        }
    }
```

* `ativo`, `page` e `limit` virarão query params automaticamente.
* Valores padrão (`= 1`, `= 10`) fazem os parâmetros serem opcionais para o cliente.
* Se você acessar:
  `/usuarios?ativo=true&page=2`
  o FastAPI cuida de converter `true` para `bool` e `2` para `int`.

Se quiser descrever melhor:

```python
from fastapi import Query

@app.get("/usuarios")
async def listar_usuarios(
    ativo: Optional[bool] = Query(None, description="Filtra por usuários ativos"),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    ...
```

---

## Rotas e endpoints em FastAPI – **Request body**

Quando você recebe dados mais estruturados (cadastro, atualização etc.), o ideal é usar **modelos Pydantic**.

Exemplo: cadastro de usuário.

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    idade: int | None = None

@app.post("/usuarios")
async def criar_usuario(usuario: UsuarioCreate):
    # aqui você faria a persistência no banco, etc.
    return {
        "mensagem": "Usuário criado com sucesso",
        "dados": usuario
    }
```

O que acontece aqui:

* O FastAPI espera um JSON no corpo da requisição.
* Ele valida contra o `UsuarioCreate`.
* Se faltar campo obrigatório ou tipo estiver errado, responde 422 com detalhes.
* Se der tudo certo, o parâmetro `usuario` já é uma instância de `UsuarioCreate` tipada.

Exemplo de body esperado:

```json
{
  "nome": "Luciano",
  "email": "luciano@example.com",
  "idade": 30
}
```

Você também pode combinar **path + query + body** na mesma função sem drama.

---

## Rotas e endpoints em FastAPI – **Cookies e Headers**

Além de path e query, você pode ler:

* **headers** → úteis para auth (Authorization), versionamento, custom flags etc.
* **cookies** → sessão, preferências etc. (mais comum quando tem front web)

### Headers

```python
from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.get("/me")
async def obter_perfil(authorization: Optional[str] = Header(None)):
    return {"authorization_header": authorization}
```

Se você mandar o header:

```http
Authorization: Bearer 123abc
```

O FastAPI injeta isso em `authorization`.

Também é comum definir:

```python
x_request_id: str = Header(...)
```

para headers customizados.

### Cookies

```python
from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

@app.get("/preferencias")
async def preferencias(usuario_tema: Optional[str] = Cookie(None)):
    return {"tema": usuario_tema}
```

Se o navegador enviar um cookie `usuario_tema=dark`, você recebe `usuario_tema = "dark"`.

---

## Retornando dados em formato JSON

FastAPI já retorna JSON por padrão sempre que você retorna:

* `dict`
* `list`
* modelos Pydantic
* outros tipos “serializáveis”

Exemplos:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
async def obter_usuario(usuario_id: int):
    return Usuario(id=usuario_id, nome="Luciano")
```

Pontos importantes:

* `response_model=Usuario` garante:

  * validação de saída;
  * documentação bonita;
  * ocultação de campos se você quiser (por ex., não retornar senha).
* O FastAPI usa `jsonable_encoder` para converter tipos como `datetime`, `UUID`, etc.

Se você quiser mais controle, pode usar `JSONResponse`, mas na maioria dos casos o retorno “cru” já resolve.

---

## Organizando as rotas com `APIRouter`

Em projetos maiores, colocar todas as rotas no `main.py` vira bagunça.
Entra em cena o `APIRouter`, que permite modularizar.

Estrutura de exemplo:

```text
app/
  main.py
  routers/
    __init__.py
    usuarios.py
    produtos.py
```

### `routers/usuarios.py`

```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

class Usuario(BaseModel):
    id: int
    nome: str

@router.get("/", response_model=list[Usuario])
async def listar_usuarios():
    return [
        Usuario(id=1, nome="Alice"),
        Usuario(id=2, nome="Bob"),
    ]

@router.get("/{usuario_id}", response_model=Usuario)
async def obter_usuario(usuario_id: int):
    return Usuario(id=usuario_id, nome="Usuário Exemplo")
```

### `routers/produtos.py`

```python
from fastapi import APIRouter

router = APIRouter(prefix="/produtos", tags=["produtos"])

@router.get("/")
async def listar_produtos():
    return [{"id": 1, "nome": "Mouse"}]
```

### `main.py`

```python
from fastapi import FastAPI
from app.routers import usuarios, produtos

app = FastAPI(title="Minha API Modularizada")

app.include_router(usuarios.router)
app.include_router(produtos.router)
```

Benefícios dessa abordagem:

* você separa domínios de negócio por arquivo/módulo;
* rota `/usuarios` vive em `usuarios.py`, `/produtos` em `produtos.py`;
* `tags` ajudam na documentação visual (Swagger agrupa endpoints por tag).

Você ainda pode:

* ter prefixo global de versão:
  `APIRouter(prefix="/v1/usuarios", ...)`
* montar routers com prefixos específicos:
  por exemplo, `/admin`, `/public`, `/internal`.

---

Em resumo:

* o `FastAPI` te dá um encaixe muito natural entre **conceitos REST** (recursos, verbos, parâmetros) e **tipagem Python**;
* path, query, body, headers e cookies são só diferentes “fontes de dados” mapeadas para parâmetros da função;
* `APIRouter` é o passo essencial para sair do “app de exemplo” para algo com cara de projeto real.
