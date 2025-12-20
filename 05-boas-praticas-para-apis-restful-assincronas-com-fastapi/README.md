# Boas Práticas para APIs RESTfull Assíncronas com FastAPI

## Tratamento de erros (sem vazar o cérebro do sistema)

Erro faz parte do fluxo normal. O problema não é errar; é **errar mal**.

### Use códigos HTTP corretos

* **400**: requisição inválida (payload errado)
* **401**: não autenticado
* **403**: autenticado, sem permissão
* **404**: recurso inexistente
* **409**: conflito (duplicidade)
* **422**: validação (o FastAPI já ajuda muito aqui)
* **500**: erro interno (nunca explique demais)

### Centralize exceções

Crie *exception handlers* para padronizar respostas:

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # log interno aqui
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno do servidor"}
    )
```

Benefício:

* respostas consistentes;
* segurança (sem stack trace);
* logs internos ricos, respostas externas simples.

---

## Documentação automática (faça dela um contrato)

FastAPI gera documentação **OpenAPI** automaticamente. Isso é ouro — trate como contrato, não como bônus.

Boas práticas:

* defina `title`, `version`, `description` no app;
* use `response_model` sempre que possível;
* documente erros comuns com `responses={}`.

Exemplo:

```python
@app.get(
    "/usuarios/{id}",
    response_model=UsuarioResponse,
    responses={404: {"description": "Usuário não encontrado"}}
)
async def obter_usuario(id: int):
    ...
```

Resultado:

* Swagger útil;
* consumidores da API entendem o que esperar;
* menos mal-entendidos entre backend e frontend.

---

## Resolvendo o problema de CORS (sem gambiarra)

CORS não é bug, é **regra de segurança do navegador**.
A API precisa dizer *quem pode chamá-la*.

No FastAPI, resolva isso explicitamente:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://meufrontend.com",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Boas práticas:

* **nunca** use `allow_origins=["*"]` em produção com credenciais;
* seja explícito sobre domínios;
* CORS é configuração, não lógica de negócio.

---

## Adicionando `pydantic-settings` ao projeto

Configuração não é código.
Misturar os dois cria sistemas frágeis.

`pydantic-settings` resolve isso com elegância.

### Instalação

```bash
poetry add pydantic-settings
```

### Criando um módulo de settings

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
```

Agora você usa:

```python
settings.database_url
```

Benefícios:

* validação automática das configs;
* erro cedo se faltar variável;
* separação clara entre ambiente e lógica.

---

## Configurando o Alembic (sem medo de mudar schema)

Se você usa banco relacional em produção, **migração é obrigatória**.

Alembic é o padrão no ecossistema SQLAlchemy.

### Inicialização

```bash
alembic init alembic
```

### Ajustes essenciais

* apontar `DATABASE_URL` para env var;
* importar `Base.metadata` dos seus modelos;
* ativar autogenerate com consciência.

Fluxo saudável:

1. altera modelo ORM;
2. gera migração:

   ```bash
   alembic revision --autogenerate -m "descricao"
   ```
3. revisa o script (sempre);
4. aplica:

   ```bash
   alembic upgrade head
   ```

Regra de ouro:

> **Nunca altere schema direto em produção sem migração versionada.**

---

## Script de reinicialização no Render (o detalhe que evita dor)

No **Render**, cada deploy reinicia o serviço.
Esse é o momento ideal para **garantir que o banco esteja no estado certo**.

Uma prática comum e segura:

### Criar um script de startup

`scripts/start.sh`:

```bash
#!/usr/bin/env bash

echo "Aplicando migrações..."
alembic upgrade head

echo "Iniciando aplicação..."
gunicorn app.main:app -k uvicorn.workers.UvicornWorker
```

No Render:

* **Start Command**:

  ```bash
  bash scripts/start.sh
  ```

Resultado:

* banco sempre migrado antes da API subir;
* deploy previsível;
* menos surpresas pós-release.

---

## A visão de conjunto (o que realmente importa)

Essas boas práticas resolvem problemas reais:

* **tratamento de erros** → segurança e previsibilidade
* **documentação automática** → contrato claro
* **CORS** → integração frontend sem fricção
* **pydantic-settings** → configuração limpa e validada
* **Alembic** → evolução segura do banco
* **script no Render** → deploy repetível e confiável

FastAPI dá as ferramentas.
Essas práticas dão **longevidade**.

Quando você aplica tudo isso, sua API deixa de ser “funcional” e passa a ser **infraestrutura confiável** — do tipo que aceita mudanças sem quebrar, cresce sem drama e dorme tranquila em produção.
