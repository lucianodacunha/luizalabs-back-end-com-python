# Gerenciamento de Pacotes, Convenções e Boas Práticas em Python

## 1. O que são pacotes e o uso do `pip`

### Pacotes

Um **pacote** é basicamente um conjunto de módulos (arquivos `.py`) organizado para ser reutilizado.
Exemplos:

* `requests` – HTTP
* `pandas` – análise de dados
* `fastapi` – APIs web
* `geopandas` – SIG com Python

Você instala esses pacotes no seu ambiente Python para não reinventar roda.

### `pip`

`pip` é o **gerenciador de pacotes padrão** do Python.
Com ele você:

* instala
* atualiza
* remove
* lista dependências

Comandos básicos:

```bash
# instalar pacote
pip install requests

# instalar versão específica
pip install "requests==2.31.0"

# atualizar
pip install -U requests

# listar pacotes instalados
pip list

# congelar (listar com versões)
pip freeze
```

Geralmente, para projetos, salvamos as dependências num **`requirements.txt`**:

```bash
pip freeze > requirements.txt
```

E para replicar em outro ambiente:

```bash
pip install -r requirements.txt
```

Combinação “clássica”:
**`venv` + `pip` + `requirements.txt`**.

---

## 2. Gerenciando dependências com **Pipenv**

O **Pipenv** foi criado para juntar:

* gerenciamento de ambiente virtual
* gerenciamento de dependências
* lockfile (garantir versões exatas)

Ele cria:

* `Pipfile` – lista de dependências (tipo manifest)
* `Pipfile.lock` – versões exatas, para reprodutibilidade

### Fluxo típico com Pipenv

Instalar:

```bash
pip install pipenv
```

Criar projeto + ambiente:

```bash
pipenv install requests
```

Isso:

* cria um ambiente virtual automático
* adiciona `requests` no `Pipfile`
* gera/atualiza o `Pipfile.lock`

Entrar no ambiente:

```bash
pipenv shell
```

Instalar dependências de desenvolvimento:

```bash
pipenv install black --dev
```

Recriar ambiente em outra máquina:

```bash
pipenv install
```

Pipenv é uma espécie de “pip + venv + requirements.txt com mais ergonomia”, mas hoje tem perdido espaço para o Poetry em muitos projetos.
---

# Erro no pipenv clean: No such file or directory

## 🧩 O que está acontecendo nesse erro?

Você rodou:

```bash
pipenv clean
```

E o pipenv começou a desinstalar pacotes:

```text
Uninstalling asgiref...
Uninstalling filelock...
Uninstalling certifi...
Uninstalling pipenv...
Uninstalling virtualenv...
```

Até aqui, tudo “normal” pro `pipenv clean`: ele remove pacotes que **não estão no Pipfile.lock**.

Só que aí vem a parte problemática:

```text
Error running command: $ "/home/.../.venv-pipenv/bin/python" "/home/.../.venv-pipenv/lib/python3.12/site-packages/pipenv/patched/pip" uninstall virtualenv -y
STDERR: ... can't open file '.../pipenv/patched/pip': [Errno 2] No such file or directory
```

Tradução:

> “Tentei rodar o pip interno do pipenv (`pipenv/patched/pip`), mas esse arquivo não existe mais.”

Ou seja:
o `pipenv clean` **começou a desinstalar coisas dentro do próprio ambiente virtual onde o pipenv está instalado**, inclusive o *próprio* pipenv e o pip “patchado” que ele usa.
Quando chegou a vez de desinstalar `virtualenv`, o pip que ele queria usar já tinha sido removido → daí o `[Errno 2] No such file or directory`.

E tem mais uma pista importante bem no começo:

```text
Pipenv found itself running within a virtual environment, so it will automatically use that environment
```

Você estava com **o venv ativado**:

```bash
(.venv-pipenv) luciano@factory$
```

Ou seja:

* Você já estava dentro de um ambiente virtual (`.venv-pipenv`)
* E rodou `pipenv clean` ali dentro
* Esse ambiente parece ter o próprio `pipenv` instalado como pacote do projeto
* Então o `pipenv clean` tentou desinstalar `pipenv` e `virtualenv` de dentro de si mesmo
  → e quebrou o pip interno no meio do processo

Clássico caso de “serrando o galho em que está sentado” 😅

---

## 🔧 O que isso significa na prática?

1. **Não é erro da sua lógica Python**, é mais um “auto-tiro no pé” do ambiente.
2. O seu ambiente `.venv-pipenv` provavelmente ficou **corrompido** (pipenv/patched/pip sumiu).
3. Isso aconteceu porque:

   * você está rodando `pipenv` *dentro* de um venv
   * e/ou `pipenv` foi instalado como dependência daquele projeto (o que não é o ideal)

---

## ✅ Caminho simples pra resolver

### 1. Desapega desse venv e recria

Na pasta do projeto:

```bash
deactivate  # se ainda estiver no venv
rm -rf .venv-pipenv
```

Depois:

* se quiser usar **pipenv**, do jeito certo:

  ```bash
  pipenv install  # cria novo ambiente com base no Pipfile
  pipenv shell
  ```

* se estiver só testando e quiser seguir com **venv normal + pip**, pode abandonar o pipenv nesse projeto.

---

### 2. Não instale `pipenv` como dependência do projeto

No `Pipfile`, veja se tem algo assim:

```toml
[packages]
pipenv = "*"
virtualenv = "*"
```

Se tiver, remova.
`pipenv` é ferramenta de **gestão do projeto**, não dependência do próprio projeto.

---

### 3. Evite rodar `pipenv` dentro de um venv já ativado

O ideal é:

* **pipenv instalado globalmente** (via `pipx` ou `pip` do sistema/pyenv)
* você roda `pipenv` **sem ativar venv antes**
* ele mesmo cria/gera o ambiente

Senha mental:

> ou eu deixo o `pipenv` cuidar do venv,
> ou eu cuido do venv “na mão” com `python -m venv`.
> Misturar os dois → bagunça.

---

## 💡 Dica extra de fluxo mais tranquilo

Pra sua trilha de estudos do bootcamp, algo assim costuma ser bem confortável:

* Projetos simples → `venv + pip + requirements.txt`
* Projetos que você quer organizar muito bem → `Poetry`

Pipenv funciona, mas tem umas pegadinhas de uso (tipo essa de rodar dentro de venv), então às vezes gera mais atrito do que ajuda.

---

## 3. Gerenciando dependências com **Poetry**

O **Poetry** leva o gerenciamento de dependências para um nível mais organizado e moderno.
Ele trabalha com:

* `pyproject.toml` – arquivo padrão PEP 621 pra metadados + dependências
* `poetry.lock` – lockfile com versões exatas

Diferenciais:

* pensa o projeto como **pacote**, não só como “pasta de scripts”
* facilita publicar no PyPI
* cuida do ambiente virtual pra você (se quiser)

### Fluxo típico com Poetry

Instalar (forma comum):

```bash
pip install poetry
# ou instalador oficial, dependendo da doc atual
```

Criar um novo projeto:

```bash
poetry new meu_projeto
```

Adicionar dependências:

```bash
poetry add requests
poetry add fastapi uvicorn
```

Dependências de desenvolvimento:

```bash
poetry add --dev black ruff pytest
```

Criar/usar o ambiente virtual e entrar nele:

```bash
poetry shell
```

Executar comandos dentro do ambiente, sem ativar manualmente:

```bash
poetry run python main.py
```

Instalar tudo em outra máquina:

```bash
poetry install
```

O Poetry está muito alinhado com o “Python moderno”:
um arquivo `pyproject.toml` centralizando config de:

* dependências
* ferramentas (black, isort, ruff, mypy…)
* versão mínima de Python
* metadados do projeto

---

## 4. Boas práticas

Agora a parte que separa o caos da sanidade.

### 🔹 Use ambientes virtuais (sempre)

Por projeto, crie um ambiente isolado:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\activate   # Windows
```

Ou deixe Pipenv/Poetry gerenciar isso.

**Nunca** instale tudo com `pip` direto no sistema global.

---

### 🔹 Registre dependências de forma explícita

Escolha um dos modelos:

* `requirements.txt` (pip)
* `Pipfile` + `Pipfile.lock` (Pipenv)
* `pyproject.toml` + `poetry.lock` (Poetry)

E mantenha isso versionado no Git (exceto o próprio venv, que entra no `.gitignore`).

---

### 🔹 Fixe versões (ou no mínimo intervalos sensatos)

Para projetos reprodutíveis, use versões travadas:

```txt
requests==2.31.0
fastapi==0.115.0
```

Ou, no Poetry, controlando na seção `[tool.poetry.dependencies]`.

Isso evita surpresas quando uma lib lança uma versão nova quebrando compatibilidade.

---

### 🔹 Separe dependências “normais” e “de desenvolvimento”

Exemplos de dev-only:

* `pytest`
* `black`
* `ruff`
* `mypy`

No Poetry:

```bash
poetry add --dev pytest black ruff
```

No pip:

* usar um `requirements-dev.txt` separado.

---

### 🔹 Não misture gerenciadores

Evite:

* usar `pipenv` e depois `poetry` no mesmo projeto
* usar `pip` direto num venv já gerenciado pelo Poetry (sem saber o que está fazendo)

Escolha **um fluxo por projeto**:

* simples? `venv + pip + requirements.txt`
* mais organizado? `Poetry`
* gosta do Pipenv? beleza, mas não misture.

---

### 🔹 Use arquivos de configuração pra ferramentas

Centralize configurações em arquivos como:

* `pyproject.toml` (Poetry + configs de tools)
* `setup.cfg` / `tox.ini` (legado, mas ainda comum)

Isso evita “bagunça de configs” espalhadas.

---

### 🔹 Documente como rodar o projeto

No `README.md`, descreva:

```bash
# com pip + venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py

# ou com poetry
poetry install
poetry run python main.py
```

O projeto não é só código: é também a forma de rodá-lo.

---

### Quando usar o quê (resumão honesto)

* **Estudo, scripts simples, bootcamps**
  → `venv + pip + requirements.txt` resolve lindamente.

* **Projetos que você pretende empacotar, publicar, organizar bem**
  → **Poetry** é uma ótima escolha.

* **Você já está num ambiente que usa Pipenv ou prefere o fluxo dele**
  → Sem problemas, use Pipenv consistentemente.

A moral: gerenciamento de dependências não é glamour, mas é o que separa um ambiente saudável de um “funciona só na minha máquina”.

---

Kit padrão” de projeto Python, cobrindo:

* `.venv` gerenciado por você
* `requirements.txt` (incluindo dev)
* alternativa com **Poetry**

A ideia é: você escolher um fluxo por projeto e seguir nele com consistência. Vou focar num contexto bem prático, como se fosse pro seu repositório do bootcamp.

---

## 1. Organização básica do projeto

Sugestão de estrutura bem saudável:

```text
meu-projeto/
├── .venv/                 # ambiente virtual (não vai pro git)
├── src/                   # seu código-fonte
│   └── main.py
├── tests/                 # (opcional) testes
├── requirements.txt       # dependências de produção/uso
├── requirements-dev.txt   # dependências de desenvolvimento
├── README.md
└── .gitignore
```

No `.gitignore`, sempre algo assim:

```gitignore
.venv/
__pycache__/
*.pyc
```

Agora vamos para os três pontos: **.venv + pip**, **requirements**, **Poetry**.

---

## 2. `.venv` gerenciado por você + `pip` (fluxo clássico e sólido)

Esse é o fluxo “canivete suíço”: simples, confiável e perfeito pra bootcamps, estudos e muitos projetos reais.

### 2.1. Criar o ambiente virtual `.venv`

Na raiz do projeto:

```bash
python -m venv .venv
```

Ou, se estiver usando `pyenv` / várias versões, algo tipo:

```bash
python3.12 -m venv .venv
```

### 2.2. Ativar o ambiente

* **Linux / macOS:**

  ```bash
  source .venv/bin/activate
  ```

* **Windows (PowerShell):**

  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

Você vai ver algo assim no prompt:

```bash
(.venv) luciano@factory$
```

Isso significa: tudo que você instalar com `pip` agora fica **isolado dentro do `.venv`**, não polui o sistema.

### 2.3. Instalar dependências

Exemplo:

```bash
pip install requests fastapi uvicorn
```

### 2.4. Gerar o `requirements.txt`

Depois que instalar o que precisa:

```bash
pip freeze > requirements.txt
```

Ele vai conter algo como:

```text
fastapi==0.115.0
requests==2.31.0
uvicorn==0.30.1
```

### 2.5. Reinstalar tudo em outra máquina

Clonou o repo? Aí é:

```bash
python -m venv .venv
source .venv/bin/activate  # ou equivalente no Windows
pip install -r requirements.txt
```

Pronto, ambiente replicado.

---

## 3. `requirements.txt` e `requirements-dev.txt` (separando produção e dev)

Boa prática: separar dependências **da aplicação** das ferramentas **de desenvolvimento** (lint, formatação, testes).

### 3.1. Exemplo

`requirements.txt` (só o que o app precisa pra rodar):

```text
fastapi==0.115.0
uvicorn==0.30.1
```

`requirements-dev.txt` (ferramentas para você trabalhar melhor):

```text
-r requirements.txt   # importa o de cima

black==24.3.0
flake8==7.0.0
isort==5.13.0
pytest==8.3.0
```

Aí, pra instalar tudo no ambiente de dev:

```bash
pip install -r requirements-dev.txt
```

Isso é ótimo pra projetos que podem ter um “modo produção” (só `requirements.txt`) e um “modo desenvolvedor” (com tudo).

---

## 4. Poetry – o fluxo mais moderno e organizado

Se você quiser subir um degrau em organização e “projeto como pacote”, o **Poetry** entra muito bem.

Ele cuida de:

* **ambiente virtual**
* **dependências**
* **lockfile** (`poetry.lock`)
* metadata do projeto
* publicação no PyPI (no futuro)

E usa um arquivo central: `pyproject.toml`.

### 4.1. Instalar o Poetry

Se ainda não tem:

```bash
pip install poetry
```

(Existe instalador oficial, mas pra estudo esse caminho já resolve.)

### 4.2. Inicializar o projeto com Poetry

Na raiz do projeto:

```bash
poetry init
```

Ele vai te perguntar:

* nome do projeto
* versão
* descrição
* dependências, etc.

Você pode aceitar o básico e depois ajustar o `pyproject.toml`.

Ou pode ir direto:

```bash
poetry new meu_projeto
```

Isso já cria uma estrutura parecida com:

```text
meu_projeto/
├── pyproject.toml
├── README.md
├── meu_projeto/
│   └── __init__.py
└── tests/
```

### 4.3. Adicionar dependências

```bash
poetry add fastapi uvicorn
```

Isso atualiza o `pyproject.toml` e o `poetry.lock`.

Dependências de desenvolvimento:

```bash
poetry add --dev black isort flake8 pytest
```

### 4.4. Ambiente virtual com Poetry

Poetry normalmente cria e gerencia um venv **pra você** (geralmente fora da pasta do projeto).

Você pode:

* entrar no venv:

  ```bash
  poetry shell
  ```

* rodar comandos dentro do ambiente sem entrar:

  ```bash
  poetry run python src/main.py
  poetry run pytest
  ```

### 4.5. Recriar ambiente em outra máquina

Depois de clonar o repo:

```bash
poetry install
```

Ele lê o `poetry.lock` e instala as mesmas versões.

---

## 5. Como escolher entre `.venv+pip` e Poetry?

### `.venv + pip + requirements.txt` é excelente quando:

* você está estudando / fazendo bootcamp
* não precisa publicar o projeto como pacote
* quer algo simples, transparente e fácil de entender
* está confortável com `pip` e `venv`

É **perfeito** pro momento em que você está.

### Poetry brilha quando:

* você quer mais organização e reprodutibilidade
* pretende transformar o projeto em **pacote** instalável
* quer centralizar configs (formatação, lint etc.) em `pyproject.toml`
* está topando uma curva de aprendizado um pouquinho maior agora pra colher benefícios depois

Um bom caminho é:

* usar **.venv + pip + requirements** nos projetos do bootcamp
* ir trazendo **Poetry** em projetos pessoais mais elaborados
* e, aos poucos, você decide onde ele encaixa melhor no seu fluxo.

---

## 6. Boas práticas gerais que valem pros dois mundos

1. **Um gerenciador por projeto**
   Ou você deixa o Poetry cuidar do venv, ou você cuida manualmente com `venv+pip`.
   Misturar `pipenv`, `Poetry`, `venv` e `conda` no mesmo projeto só traz caos.

2. **Sempre usar `.venv` no `.gitignore`**
   Ambiente não vai pro Git, só a “receita” (requirements ou pyproject/lock).

3. **Documentar como rodar o projeto**
   No `README.md`, algo como:

   Para venv+pip:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   python src/main.py
   ```

   Para Poetry:

   ```bash
   poetry install
   poetry run python src/main.py
   ```

4. **Padronizar ferramenta de formatação/lint**
   Black, isort, flake8/ruff → deixam seu código consistente em qualquer máquina.
