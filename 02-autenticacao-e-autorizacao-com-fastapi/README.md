# Autenticação e Autorização com FastAPI

## Autenticação vs Autorização (alinhando o vocabulário)

Antes de qualquer código, o mapa conceitual:

* **Autenticação** → *“Quem é você?”*
  Ex.: validar usuário e senha, emitir um token.

* **Autorização** → *“O que você pode fazer?”*
  Ex.: este usuário pode acessar este endpoint? Pode apagar dados? Pode ver dados de outros?

Tokens resolvem **autenticação**.
Autorização vem depois, construída em cima da identidade validada.

---

## Por que usar autenticação baseada em token?

Em APIs RESTful, especialmente assíncronas:

* não há sessão de servidor (stateless);
* cada requisição deve carregar sua identidade;
* a API deve escalar horizontalmente sem “memória compartilhada”.

Tokens resolvem isso porque:

* são enviados a cada requisição;
* carregam informações básicas do usuário;
* podem ser validados sem acessar o banco (dependendo da estratégia).

O padrão mais comum: **JWT (JSON Web Token)**.

---

## O que é um JWT?

Um JWT é uma string composta por três partes:

```
header.payload.signature
```

Exemplo (encurtado):

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjMiLCJlbWFpbCI6InVzZXJAZW1haWwuY29tIn0.
abc123...
```

Conceitualmente:

* **header** → algoritmo de assinatura
* **payload** → dados (claims)
* **signature** → garante que o token não foi alterado

O servidor **assina** o token.
O cliente **não consegue falsificar** um token válido sem a chave secreta.

---

## Fluxo clássico de autenticação com token

1. Usuário envia `email + senha`
2. API valida credenciais
3. API gera um token JWT
4. Cliente armazena o token (normalmente em memória ou storage seguro)
5. Cliente envia o token no header `Authorization`
6. API valida o token a cada requisição protegida

Fluxo simples, previsível e escalável.

---

## Stack típica no FastAPI

Para JWT com FastAPI, o conjunto mais comum é:

* `fastapi`
* `python-jose` (JWT)
* `passlib` (hash de senha)
* `OAuth2PasswordBearer` (fluxo padrão)

Isso não significa OAuth completo — é só o **formato do fluxo**.

---

## Hash de senha (nunca armazene senha pura)

Antes de falar de token, um ponto **crítico**:

> Senhas nunca são armazenadas em texto puro.

Usamos hash:

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return pwd_context.verify(senha, hash_salvo)
```

O banco guarda o **hash**, nunca a senha.

---

## Configuração básica do JWT

```python
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "chave-super-secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

Essa chave deve:

* ficar fora do código (env var em produção);
* nunca ser compartilhada.

---

## Criando o token de acesso

```python
def criar_token(dados: dict, expires_delta: timedelta | None = None):
    to_encode = dados.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

Normalmente você inclui no payload:

* `sub` (subject → id do usuário)
* talvez email ou role

Exemplo:

```python
token = criar_token({"sub": str(usuario.id)})
```

---

## Endpoint de login (autenticação)

FastAPI já traz um helper padrão:

```python
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
```

```python
@app.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = buscar_usuario_por_email(form_data.username)

    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token({"sub": str(usuario.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
```

Observação importante:

* `username` aqui pode ser email (nome histórico do padrão OAuth2).

---

## Enviando o token nas requisições

O cliente deve enviar:

```
Authorization: Bearer <token>
```

Exemplo:

```
GET /usuarios
Authorization: Bearer eyJhbGciOi...
```

---

## Validando o token (dependência de segurança)

Aqui entra a parte elegante do FastAPI: **Dependencies**.

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
```

```python
from jose import JWTError

async def get_usuario_atual(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = buscar_usuario_por_id(user_id)
    if not usuario:
        raise HTTPException(status_code=401)

    return usuario
```

Essa função:

* extrai o token do header;
* valida assinatura e expiração;
* retorna o usuário autenticado.

---

## Protegendo rotas (autorização básica)

Agora é só usar a dependência:

```python
@app.get("/me")
async def perfil(usuario=Depends(get_usuario_atual)):
    return {
        "id": usuario.id,
        "email": usuario.email
    }
```

Se não tiver token:

* 401 automaticamente.

Se tiver token inválido:

* 401.

Aqui você já tem **autenticação funcional**.

---

## Autorização (roles, permissões)

Autorização é construída em cima do usuário autenticado.

Exemplo simples:

```python
def exigir_admin(usuario=Depends(get_usuario_atual)):
    if usuario.role != "admin":
        raise HTTPException(status_code=403)
    return usuario
```

```python
@app.delete("/usuarios/{id}")
async def deletar_usuario(
    id: int,
    usuario=Depends(exigir_admin)
):
    ...
```

* 401 → não autenticado
* 403 → autenticado, mas sem permissão

Semântica correta de HTTP.

---

## Boas práticas essenciais

Algumas regras que evitam dor futura:

* tokens devem expirar;
* segredo nunca fica no código;
* não confie em dados sensíveis no payload do JWT;
* use HTTPS sempre;
* prefira tokens curtos + refresh token (em sistemas maiores);
* trate autenticação como infraestrutura, não feature isolada.

---

## O quadro geral

Com FastAPI + JWT você tem:

* API stateless;
* autenticação escalável;
* integração fácil com front, mobile, outros serviços;
* controle fino de autorização via dependencies.

O ponto mais importante:
**FastAPI não impõe segurança, ele fornece os encaixes corretos.**
Quem decide a política é você.

Daqui pra frente, os próximos níveis naturais são:

* refresh tokens;
* revogação de tokens;
* autenticação por terceiros (OAuth2 real);
* testes de segurança automatizados.

Mas com o que você viu aqui, já dá para construir **APIs seguras e profissionais**, sem truques obscuros nem mágica enganosa.
