# Deploy de uma API FastAPI Assíncrona

Deploy é o momento em que a API sai do laboratório e encara o mundo real — vento, tráfego, concorrência e usuários imprevisíveis.
Aqui o discurso muda: menos “como funciona” e mais **“como não quebrar em produção”**. Vamos caminhar do zero até uma API FastAPI assíncrona rodando com dignidade.

Vou estruturar como um **guia mental de deploy**, não como receita engessada, porque as decisões importam mais que os comandos.

---

## Criando o repositório e preparando o servidor web

### Repositório: código que sabe onde está

Antes de qualquer servidor, o projeto precisa estar **bem organizado e versionado**.

Estrutura mínima saudável:

```text
app/
  main.py
  routers/
  models/
  database.py
tests/
pyproject.toml
README.md
.env.example
```

Boas práticas aqui:

* nada de segredo no repositório;
* `.env.example` documenta variáveis necessárias;
* `README.md` explica como rodar localmente.

Versionamento (Git):

* commits pequenos e claros;
* branch principal estável;
* deploy sempre parte de um commit conhecido.

---

### Escolhendo o servidor

Para FastAPI assíncrono, o stack clássico e confiável é:

* **Uvicorn** → servidor ASGI
* **Gunicorn + UvicornWorker** → produção com múltiplos workers
* **Nginx** → proxy reverso (opcional, mas recomendado)

Arquitetura típica:

```
Internet
   ↓
Nginx
   ↓
Gunicorn (Uvicorn workers)
   ↓
FastAPI
```

Isso separa responsabilidades:

* Nginx lida com HTTP “sujo” (TLS, headers, buffer);
* Gunicorn gerencia processos;
* FastAPI só cuida da aplicação.

---

### Rodando a API em produção

Exemplo de comando típico:

```bash
gunicorn app.main:app \
  -k uvicorn.workers.UvicornWorker \
  -w 4 \
  -b 0.0.0.0:8000
```

Pontos importantes:

* `-w 4` → número de workers (depende da máquina);
* FastAPI continua assíncrona **dentro de cada worker**;
* não use `--reload` em produção.

Isso já resolve 80% dos cenários reais.

---

## Criando o banco de dados

Aqui mora uma das maiores fontes de bugs em deploy.

### Banco local ≠ banco de produção

Em desenvolvimento:

* SQLite é prático;
* arquivo local;
* zero setup.

Em produção:

* SQLite só funciona em cenários muito simples;
* concorrência real pede banco servidor.

Escolhas comuns:

* PostgreSQL (o padrão de ouro);
* MySQL/MariaDB;
* SQL Server (ambiente corporativo).

---

### Criando o banco

Passos típicos (conceitualmente):

1. subir o serviço de banco (cloud, VM ou container);
2. criar o banco e o usuário;
3. conceder permissões mínimas;
4. configurar URL de conexão.

Exemplo de URL (PostgreSQL):

```text
postgresql+asyncpg://usuario:senha@host:5432/meubanco
```

Essa URL **não fica no código**.

---

### Variáveis de ambiente

Em produção, tudo que muda por ambiente vira variável:

```env
DATABASE_URL=postgresql+asyncpg://...
SECRET_KEY=chave-super-secreta
ENV=production
```

No FastAPI:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

Isso permite:

* trocar banco sem alterar código;
* subir múltiplos ambientes (dev, staging, prod).

---

## Ajustando o “problema com o CRUD” (o ponto crítico)

Esse tópico é excelente, porque quase todo mundo tropeça aqui.

### O problema clássico

Localmente:

* você cria tabelas com `Base.metadata.create_all()`;
* tudo funciona.

Em produção:

* banco já existe;
* esquema muda com o tempo;
* `create_all()` não resolve migração.

Resultado:

* deploy quebra;
* dados ficam inconsistentes;
* pânico.

---

### A regra de ouro

> **Nunca confie em `create_all()` como estratégia de evolução de schema em produção.**

Ele serve para:

* testes;
* protótipos;
* ambientes descartáveis.

---

### Solução correta: migração de banco

Mesmo que você não entre em detalhes agora, o conceito é essencial:

* schema do banco **versionado**;
* alterações aplicadas de forma incremental;
* histórico de mudanças controlado.

Fluxo mental correto:

1. modelo ORM muda;
2. migração é gerada;
3. migração é aplicada no banco;
4. API sobe.

Isso evita o famoso:

> “na minha máquina funciona”.

---

### CRUD e concorrência em produção

Outro problema comum:
CRUD que funciona localmente começa a falhar sob carga.

Causas frequentes:

* sessão compartilhada incorretamente;
* conexões não fechadas;
* uso de driver síncrono em endpoint `async`;
* transações mal definidas.

Checklist saudável:

* uma sessão por request;
* engine assíncrono;
* `async with session`;
* commit e rollback explícitos;
* tratamento de exceções.

Se isso já foi bem feito no código (como você estudou antes), o deploy não vira surpresa.

---

## Fluxo completo de deploy (visão de cima)

O processo completo, mentalmente, fica assim:

1. **Código**

   * API testada
   * testes passando
   * dependências fixadas

2. **Repositório**

   * commit estável
   * tags ou versões claras

3. **Servidor**

   * ambiente virtual isolado
   * variáveis de ambiente configuradas
   * Gunicorn + Uvicorn

4. **Banco**

   * banco criado
   * schema migrado
   * credenciais seguras

5. **Inicialização**

   * API sobe
   * health check responde
   * logs funcionando

6. **Monitoramento**

   * logs centralizados
   * erros observáveis
   * métricas básicas

Deploy não é um evento.
É um **processo repetível**.

---

## Erros comuns que valem evitar

Algumas armadilhas clássicas:

* rodar FastAPI direto com `uvicorn --reload` em produção;
* usar SQLite com múltiplos workers sem entender limitações;
* deixar segredo no código;
* criar tabelas automaticamente em produção;
* não testar autenticação antes do deploy;
* não ter rota de health check.

Esses erros não são teóricos — são experiências compartilhadas da indústria.

---

## A visão madura do deploy

Deploy não é glamour.
É disciplina.

Quando bem feito:

* a API sobe sem drama;
* bugs são previsíveis;
* rollback é possível;
* crescer não dá medo.

FastAPI te dá a performance e a estrutura.
Mas **deploy é engenharia**, não framework.

E quando você entende isso, o backend deixa de ser frágil e passa a ser **infraestrutura confiável** — exatamente o tipo de sistema que aguenta o mundo real sem pedir desculpas.

## Deploy com Render - Adicional

Deploy no **Render** é quase um antídoto contra a fadiga de DevOps. Ele fica naquele ponto doce entre *“não quero mexer com servidor”* e *“quero algo mais sério que um brinquedo”*. Vamos entender o **como** e, mais importante, o **porquê**.

---

## O que é o Render (e por que ele é atraente)

Render é uma plataforma de **PaaS (Platform as a Service)**.
Tradução prática: você entrega o repositório, ele entrega a infraestrutura.

Ele cuida automaticamente de:

* build da aplicação;
* provisionamento de servidor;
* HTTPS;
* restart automático;
* variáveis de ambiente;
* integração com GitHub/GitLab.

Para APIs FastAPI assíncronas, ele encaixa muito bem porque:

* suporta ASGI (Uvicorn/Gunicorn);
* funciona bem com bancos externos;
* tem deploy automático por commit.

É uma ponte elegante entre *local funcionando* e *produção acessível*.

---

## Fluxo mental do deploy no Render

Antes dos detalhes técnicos, vale entender o **fluxo conceitual**, que é sempre o mesmo:

1. Código versionado no Git
2. Render conecta no repositório
3. Você descreve como rodar a app
4. Render constrói e executa
5. A API ganha uma URL pública

Nada de SSH, nada de servidor manual.

---

## Preparando o repositório FastAPI

Seu projeto precisa deixar claro **como ele sobe**.

Pontos essenciais:

* `main.py` com `app = FastAPI()`
* dependências declaradas (`pyproject.toml` ou `requirements.txt`)
* comando explícito para iniciar o servidor

Exemplo de comando que o Render vai rodar:

```bash
gunicorn app.main:app -k uvicorn.workers.UvicornWorker
```

O Render **não adivinha**. Você diz exatamente como subir.

---

## Criando o serviço no Render

No painel do Render, o caminho mental é:

* “New” → “Web Service”
* conectar repositório Git
* escolher branch
* definir tipo: *Web Service*
* definir ambiente: *Python*

Campos importantes:

* **Build Command**
  Exemplo:

  ```bash
  pip install -r requirements.txt
  ```

  ou, se usar Poetry:

  ```bash
  pip install poetry && poetry install --no-root
  ```

* **Start Command**
  Exemplo:

  ```bash
  gunicorn app.main:app -k uvicorn.workers.UvicornWorker
  ```

Isso já resolve 80% dos deploys FastAPI.

---

## Variáveis de ambiente (ponto crítico)

Nada de segredo no código.
Tudo sensível vira variável no Render:

* `DATABASE_URL`
* `SECRET_KEY`
* `ENV=production`

No painel do Render:

* seção **Environment Variables**
* chave → valor
* sem commit, sem vazamento

No código, você apenas consome:

```python
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

Isso é o que permite:

* mudar banco sem redeploy;
* separar dev / prod;
* rodar com segurança.

---

## Banco de dados no Render

Aqui há duas estratégias comuns:

### 1. Banco gerenciado pelo próprio Render

* PostgreSQL integrado
* simples de criar
* bom para projetos pequenos e médios

Ele gera automaticamente:

* host
* porta
* usuário
* senha
* URL completa

### 2. Banco externo

* Supabase, Neon, RDS, Azure, etc.
* mais controle
* mais escalável

Em ambos os casos, o princípio é o mesmo:

* Render **não cria schema**
* sua aplicação **não deve criar tabelas em produção**

O banco deve estar:

* criado;
* migrado;
* pronto antes do deploy.

---

## Ajustes importantes para CRUD em produção

Aqui entra experiência prática.

Alguns ajustes são quase obrigatórios:

* **Nada de `create_all()` automático**

  * use isso só localmente
* **Uma sessão por request**
* **Engine assíncrono**
* **Driver async compatível**
* **Tratamento explícito de erro**

O Render sobe múltiplas instâncias se necessário.
Se seu CRUD não for stateless e bem isolado, os problemas aparecem rápido.

---

## Deploy automático (o grande trunfo)

Uma das melhores partes do Render:

* commit na branch principal
* Render detecta mudança
* build automático
* restart da aplicação

Isso força uma boa disciplina:

* testes antes do commit;
* código sempre em estado “deployável”.

Deploy vira rotina, não evento traumático.

---

## Limitações e cuidados

Nada é mágico. Alguns pontos de atenção:

* plano gratuito “hiberna” após inatividade;
* cold start pode existir;
* não é o lugar ideal para workloads muito pesados;
* controle fino de infra é limitado (o que também é uma vantagem).

Render é excelente para:

* APIs REST;
* projetos pessoais;
* MVPs;
* serviços médios.

Para infra extremamente customizada, você sai do PaaS e vai para IaaS.

---

## A leitura madura do Render

Render não é “deploy fácil”.
É **deploy opinado**.

Ele assume:

* que você versiona código;
* que você separa config de código;
* que sua aplicação é stateless;
* que você respeita boas práticas.

Se você fizer sua parte, ele faz a dele — e faz bem.

No contexto de FastAPI assíncrona, Render funciona como um **campo de pouso suave**:
você sai do local, entra em produção, sem tropeçar em servidor, firewall ou TLS.

E isso libera o que realmente importa:
**tempo para evoluir a API, não para cuidar da máquina**.
