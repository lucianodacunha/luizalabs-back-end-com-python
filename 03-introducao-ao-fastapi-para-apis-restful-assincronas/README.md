## 1. Introdução ao FastAPI, suas limitações e seus benefícios

### O que é o FastAPI?

FastAPI é um framework web moderno para construir **APIs** em Python, com foco em:

* **Desempenho** (usa Starlette + Uvicorn, rodando sobre ASGI, que é o “WSGI 2.0” assíncrono);
* **Type hints** do Python como primeira classe (validação automática, geração de schema);
* **APIs REST** e **APIs assíncronas** com `async def` de forma natural;
* **Documentação automática** (OpenAPI + Swagger UI + ReDoc).

Ele foi pensado para usar o que há de mais moderno em Python:

* `async/await`;
* Pydantic (tipagem e validação de dados);
* ASGI (para lidar com I/O concorrente: requisições simultâneas, websockets etc.).

Em termos práticos: você escreve função Python, anota tipos, e ganha de brinde:

* validação de entrada;
* schema OpenAPI;
* docs interativas;
* responses JSON padronizadas.

### Benefícios (especialmente para APIs assíncronas)

Alguns pontos fortes:

**1. Desempenho e escalabilidade I/O-bound**
Quando você faz muitas operações de I/O (banco, HTTP externo, filas, etc.), o modelo assíncrono permite que a mesma instância de app lide com várias requisições enquanto espera respostas externas.
É perfeito para APIs que:

* falam com vários serviços;
* consomem bancos remotos;
* integram com APIs externas.

**2. DX – Developer Experience**
FastAPI é amigável demais para quem gosta de coisa bem pensada:

* `@app.get("/users")` → rota clara
* Tipos: `user_id: int`, `email: str`, `created_at: datetime`
* Modelos Pydantic → validação automática, docs bonitas sem esforço

Você literalmente ganha uma **UI de teste** (Swagger) acessando `/docs`.

**3. Tipagem forte e feedback rápido**
Por usar type hints pra tudo, você consegue:

* detectar erros cedo (IDE, mypy, etc.);
* entender rapidamente o contrato da API;
* gerar clientes automaticamente com base no OpenAPI.

**4. Integração com async de forma natural**

Você pode declarar handlers como:

```python
@app.get("/items")
async def list_items():
    return await service.list_items()
```

e misturar com funções síncronas quando necessário.

---

### Limitações e cuidados

Nada é bala de prata, então vale o olhar crítico:

**1. Não resolve CPU-bound por mágica**
Se você tiver tarefas pesadas de CPU (processamento de imagem, ML pesado, etc.), o modelo assíncrono não vai acelerar esses trechos.
Aí se entra em:

* processos separados;
* Celery/RQ;
* workers especializados.

**2. Exige disciplina com async/await**
Se você chamar função **bloqueante** dentro de endpoint `async def`, você perde as vantagens da assincronicidade (e pode até travar o event loop).
Exemplo de cilada:

* usar client HTTP síncrono ou driver de banco síncrono dentro de `async def`.

**3. Ecosistema “menor” em comparação a Django**
FastAPI não é “framework full stack” monolítico.
Não vem com:

* Admin pronto;
* ORM nativo;
* sistema built-in de templates, auth completo etc.

Você monta a stack escolhendo:

* ORM (SQLAlchemy, Tortoise, etc.);
* autenticação (JWT, OAuth, lib externa).

É flexível, mas exige mais decisões arquiteturais.

**4. Curva de aprendizado para quem vem de frameworks síncronos**
Entender bem:

* ASGI;
* diferença entre sync/async;
* quando usar threadpool, etc.

Mas, como você já está mirando APIs, isso joga a seu favor.

---

## 2. Instalação e configuração do ambiente com FastAPI usando Poetry

Agora a parte prática: montar um ambiente “decente” com **Poetry** gerenciando dependências.

Vou assumir:

* Python 3.10+ já instalado;
* Poetry instalado globalmente.

### 2.1. (Opcional) Conferindo Python e instalando Poetry

Ver Python:

```bash
python3 --version
```

Se o Poetry ainda não estiver instalado, o método “oficial” mais comum é:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Depois, garanta que o binário esteja no PATH (normalmente `~/.local/bin` em Linux).

```bash
poetry --version
```

Se isso funcionar, estamos prontos.

---

### 2.2. Criando o projeto FastAPI com Poetry

Vamos criar uma pasta de projeto:

```bash
mkdir minha_api_fastapi
cd minha_api_fastapi
```

Agora inicializar um projeto Poetry:

```bash
poetry init
```

Ele vai fazer perguntas:

* nome do pacote (pode ser `minha_api_fastapi`);
* versão do Python (coloque algo como `^3.11` se estiver usando 3.11);
* dependências (pode pular e adicionar depois).

Ou, se quiser algo mais automático:

```bash
poetry new minha_api_fastapi
cd minha_api_fastapi
```

Isso já cria uma estrutura assim:

```text
minha_api_fastapi/
  pyproject.toml
  README.md
  minha_api_fastapi/
      __init__.py
      # aqui colocaremos o main.py depois
  tests/
```

---

### 2.3. Definindo a versão do Python no Poetry

No `pyproject.toml`, a seção `[tool.poetry.dependencies]` deve ter algo assim:

```toml
[tool.poetry.dependencies]
python = "^3.11"
```

Se quiser forçar o uso de um Python específico:

```bash
poetry env use python3.11
```

(ou o caminho completo do binário do Python).

---

### 2.4. Instalando FastAPI e Uvicorn

Dentro da pasta do projeto:

```bash
poetry add fastapi "uvicorn[standard]"
```

Isso adiciona ao `pyproject.toml` algo como:

```toml
[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.115.0"  # exemplo de versão
uvicorn = {extras = ["standard"], version = "^0.30.0"}
```

Pronto: ambiente básico para rodar uma API FastAPI.

Se quiser já preparar para testes:

```bash
poetry add --dev pytest httpx
```

---

### 2.5. Estrutura mínima recomendada

Dentro do pacote principal (`minha_api_fastapi/`), dá para começar simples:

```text
minha_api_fastapi/
  __init__.py
  main.py
```

Conteúdo de `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Minha API Assíncrona")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Olá, {name}!"}
```

Note que os endpoints são `async def` — já estamos no modo assíncrono oficialmente 😄

---

### 2.6. Rodando o servidor com Poetry + Uvicorn

De dentro do projeto:

```bash
poetry run uvicorn minha_api_fastapi.main:app --reload
```

* `minha_api_fastapi.main:app` → `pacote.módulo:objeto_app`
* `--reload` → recarrega automaticamente quando você altera o código (ótimo para desenvolvimento).

A API deve subir em `http://127.0.0.1:8000`.

Endpoints importantes:

* `http://127.0.0.1:8000/health` → nosso health check
* `http://127.0.0.1:8000/hello/Luciano` → só pra testar
* `http://127.0.0.1:8000/docs` → Swagger UI auto-gerado
* `http://127.0.0.1:8000/redoc` → ReDoc, outra interface de documentação

---

### 2.7. Um exemplo simples de endpoint assíncrono "de verdade"

Para concretizar a ideia de I/O assíncrono, imagine algo assim:

```python
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/github/{user}")
async def get_github_user(user: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://api.github.com/users/{user}")
        resp.raise_for_status()
        data = resp.json()
    return {"login": data["login"], "public_repos": data["public_repos"]}
```

Aqui:

* usamos `httpx.AsyncClient` (cliente HTTP assíncrono);
* `await client.get(...)` libera o event loop enquanto espera a resposta;
* FastAPI cuida do resto: serialização JSON, docs e validação de tipos.

No mundo real, no lugar do GitHub entrariam:

* banco assíncrono (por exemplo, `encode/databases`, `SQLModel` com suporte async);
* outros serviços internos;
* filas, etc.
