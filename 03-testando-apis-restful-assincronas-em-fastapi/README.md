# **Testando APIs RESTful Assíncronas com FastAPI**

Aqui entramos em um território onde muita gente *acha* que testa, mas pouca gente realmente **confia** nos testes.
Testar APIs assíncronas não é só “bater no endpoint e ver se retorna 200”. É provar, de forma automatizada, que sua API:

* responde corretamente;
* respeita contratos;
* lida bem com concorrência;
* não quebra quando o mundo externo falha.

FastAPI foi desenhado já pensando nisso — e o ecossistema de testes em Python acompanha muito bem.

---

## Por que testar APIs RESTful assíncronas?

APIs assíncronas lidam com:

* múltiplas requisições simultâneas;
* I/O (banco, HTTP externo);
* dependências injetadas;
* autenticação e autorização.

Sem testes:

* refatorar vira roleta russa;
* bugs aparecem só em produção;
* você passa a “testar no braço”.

Com testes:

* você muda código com segurança;
* documenta comportamento;
* detecta regressões cedo.

Teste é **infraestrutura cognitiva**, não burocracia.

---

## Stack de testes que vamos usar

O conjunto que você citou é, hoje, o padrão moderno para FastAPI assíncrono:

* **pytest** → motor de testes
* **pytest-asyncio** → suporte a `async def` nos testes
* **httpx** → cliente HTTP assíncrono (muito melhor que requests aqui)
* **pytest-mock** → mocking simples e limpo

Cada peça resolve um problema específico — sem sobreposição inútil.

---

## Estrutura básica de testes

Uma estrutura comum e saudável:

```text
app/
  main.py
  routers/
  services/
tests/
  conftest.py
  test_usuarios.py
  test_auth.py
```

Separar testes por domínio ajuda a manter sanidade quando o projeto cresce.

---

## pytest: a base de tudo

O `pytest` funciona por convenção:

* arquivos começam com `test_`
* funções começam com `test_`
* asserts são simples (`assert x == y`)

Exemplo trivial:

```python
def test_soma_simples():
    assert 2 + 2 == 4
```

Sem classes obrigatórias, sem herança ritualística. Direto ao ponto.

---

## pytest-asyncio: testando código assíncrono

FastAPI usa `async def`.
Logo, seus testes também precisam ser assíncronos.

Com `pytest-asyncio`, você escreve:

```python
import pytest

@pytest.mark.asyncio
async def test_funcao_assincrona():
    resultado = await alguma_funcao_async()
    assert resultado == "ok"
```

Sem isso, você ficaria preso a workarounds feios.

---

## httpx: cliente HTTP assíncrono para testes

Aqui está uma decisão importante:
**não suba o servidor de verdade** para testar.

Você testa a aplicação **em memória**, via ASGI.

Exemplo básico com FastAPI:

```python
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_healthcheck():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

O que está acontecendo:

* `app=app` → usa a aplicação FastAPI diretamente
* nada escuta porta
* tudo é rápido e isolado

Isso é elegante e eficiente.

---

## Fixtures: preparando o ambiente de teste

Fixtures são funções que preparam contexto reutilizável.

Exemplo: cliente HTTP padrão.

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
```

Agora seus testes ficam limpos:

```python
@pytest.mark.asyncio
async def test_listar_usuarios(client):
    response = await client.get("/usuarios")
    assert response.status_code == 200
```

Fixtures evitam repetição e acoplamento.

---

## Testando CRUD RESTful assíncrono

### CREATE (POST)

```python
@pytest.mark.asyncio
async def test_criar_usuario(client):
    payload = {
        "nome": "Luciano",
        "email": "luciano@email.com"
    }

    response = await client.post("/usuarios", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Luciano"
```

Aqui você valida:

* status code;
* contrato de resposta;
* comportamento funcional.

---

### READ (GET)

```python
@pytest.mark.asyncio
async def test_obter_usuario_inexistente(client):
    response = await client.get("/usuarios/999")

    assert response.status_code == 404
```

Testar erro é tão importante quanto testar sucesso.

---

### UPDATE (PUT / PATCH)

```python
@pytest.mark.asyncio
async def test_atualizar_usuario(client):
    payload = {"nome": "Novo Nome"}

    response = await client.patch("/usuarios/1", json=payload)

    assert response.status_code == 200
    assert response.json()["nome"] == "Novo Nome"
```

---

### DELETE

```python
@pytest.mark.asyncio
async def test_remover_usuario(client):
    response = await client.delete("/usuarios/1")
    assert response.status_code == 204
```

Sem corpo. Sem drama. REST correto.

---

## pytest-mock: isolando dependências externas

Agora o ponto crítico: **mockar o mundo externo**.

Você **não quer**:

* chamar banco real;
* chamar API externa;
* depender de estado global.

Exemplo: mockando uma função de serviço.

```python
def test_listar_usuarios_mockado(client, mocker):
    mocker.patch(
        "app.services.usuario_service.listar_usuarios",
        return_value=[
            {"id": 1, "nome": "Mock"}
        ]
    )

    response = await client.get("/usuarios")

    assert response.status_code == 200
    assert response.json()[0]["nome"] == "Mock"
```

Aqui:

* você testa a **rota**, não o banco;
* garante isolamento;
* ganha testes rápidos e confiáveis.

---

## Mockando funções assíncronas

Para funções `async`, use `AsyncMock`:

```python
from unittest.mock import AsyncMock

mocker.patch(
    "app.services.usuario_service.listar_usuarios",
    new_callable=AsyncMock,
    return_value=[]
)
```

Isso evita warnings e comportamentos estranhos.

---

## Testando autenticação com token

Exemplo conceitual:

```python
@pytest.mark.asyncio
async def test_rota_protegida_sem_token(client):
    response = await client.get("/me")
    assert response.status_code == 401
```

Com token:

```python
headers = {
    "Authorization": f"Bearer {token_falso}"
}

response = await client.get("/me", headers=headers)
assert response.status_code in (401, 200)
```

Aqui você valida:

* proteção da rota;
* semântica HTTP correta.

---

## Boas práticas em testes de APIs assíncronas

Algumas regras que salvam tempo e sanidade:

* teste comportamento, não implementação;
* prefira muitos testes pequenos;
* mocke o que não é foco do teste;
* teste erros explicitamente;
* não compartilhe estado entre testes;
* mantenha testes rápidos (milissegundos, não segundos).

Teste lento é teste ignorado.

---

## O panorama final

Com essa stack:

* **pytest** → estrutura clara
* **pytest-asyncio** → suporte real a async
* **httpx** → cliente moderno e assíncrono
* **pytest-mock** → isolamento e controle

Você consegue:

* testar APIs FastAPI sem subir servidor;
* validar contratos REST;
* simular falhas externas;
* refatorar sem medo.

No fim das contas, testes são uma forma de respeito:
respeito pelo código, por quem vai manter depois — e por você mesmo daqui a seis meses, tentando lembrar *por que isso funciona*.
