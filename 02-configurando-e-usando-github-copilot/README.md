## **Configurando e usando o GitHub Copilot**

Aqui a ideia é bem pragmática: **instalar, configurar e usar** — sem misticismo. O Copilot funciona melhor quando você o trata como um **assistente obediente**, não como um oráculo. Você pensa; ele acelera.

---

## 1️⃣ Instalação do GitHub Copilot

### Introdução

O **GitHub Copilot** é uma extensão que vive **dentro da IDE**. Ele observa o contexto do arquivo, comentários e padrões do projeto e sugere código em tempo real. Para começar, você precisa de:

* uma conta no GitHub;
* acesso ao Copilot (plano individual, educacional ou empresarial);
* uma IDE compatível.

---

### Instalando o GitHub Copilot em IDEs

**VS Code** (o caminho mais comum):

1. Abra o VS Code
2. Vá em *Extensions*
3. Procure por **GitHub Copilot**
4. Instale e faça login no GitHub quando solicitado

**Outras IDEs**:

* **PyCharm** (Professional)
* IntelliJ IDEA
* Neovim (via plugins)
* Visual Studio

O fluxo é o mesmo: instalar a extensão e autenticar com sua conta GitHub.

Quando tudo dá certo, você percebe rápido: sugestões começam a aparecer em cinza, como se o editor estivesse “pensando junto”.

---

## 2️⃣ Configurando o GitHub Copilot

### Configurações do Copilot (menos é mais)

Depois de instalado, vale ajustar o comportamento para não virar poluição visual.

No VS Code:

* Settings → “Copilot”

Configurações comuns e úteis:

* **Habilitar/desabilitar por linguagem**
  Ex.: ativo para Python, desativado para Markdown.
* **Sugestões automáticas**
  Você pode deixar sempre ativas ou exigir confirmação.
* **Aceitar sugestão**
  Normalmente com `Tab` (músculo da produtividade).

Boa prática:
👉 comece com poucas automações e vá soltando as rédeas conforme se acostuma.

---

### Copilot funciona melhor com contexto claro

Ele é sensível a:

* nomes de funções;
* comentários bem escritos;
* estrutura do projeto.

Exemplo de comentário que ajuda muito:

```python
# cria um endpoint para listar usuários ativos com paginação
```

Isso é quase um *prompt* disfarçado. Quanto mais clara a intenção, melhor a sugestão.

---

## 3️⃣ Utilizando o GitHub Copilot na prática

Agora vamos usar o Copilot para **fazer algo real**, não só completar linha.

### Fazendo um sistema simples com o Copilot

Vamos imaginar um **mini CRUD de usuários com FastAPI**.

Você começa assim:

```python
from fastapi import FastAPI

app = FastAPI()

# endpoint para criar um usuário
```

Pare. Espere.
O Copilot provavelmente sugere:

* um `@app.post`;
* um modelo Pydantic;
* um body básico.

Você **não aceita tudo cegamente**. Aceita, ajusta, valida.

Exemplo do que costuma surgir (simplificado):

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str

@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
    return usuario
```

Agora você evolui com intenção:

```python
# endpoint para listar usuários
```

O Copilot completa algo como:

```python
@app.get("/usuarios")
async def listar_usuarios():
    return []
```

Você ajusta, melhora, conecta banco depois.
O ganho está em **não digitar o óbvio**, e sim revisar.

---

### Usos onde o Copilot realmente brilha

* criar modelos Pydantic repetitivos;
* gerar testes com pytest;
* escrever código “cerimonial” (CRUD, validação);
* adaptar padrões já existentes no projeto.

Onde ele **não** substitui você:

* decisões de arquitetura;
* regras de negócio;
* segurança;
* performance crítica.

---

## Dicas práticas para usar bem (e não virar refém)

* Leia tudo antes de aceitar
* Aceite por partes, não no impulso
* Refatore sugestões sem dó
* Use testes para validar
* Desconfie de código “bonito demais”

O Copilot acelera o teclado, não o cérebro.
Se o cérebro desligar, o risco sobe.

---

## Fechando o quadro

Configurar e usar o GitHub Copilot é menos sobre “ativar IA” e mais sobre **mudar o ritmo de trabalho**:

* você pensa em blocos maiores;
* escreve menos boilerplate;
* revisa mais do que digita;
* foca em qualidade e intenção.

Quando usado com base sólida (como você vem construindo com FastAPI, bancos, async, testes), o Copilot vira um **multiplicador de produtividade**, não um atalho perigoso.

Ele não programa por você.
Ele **acompanha** — e quem dirige continua sendo você.
