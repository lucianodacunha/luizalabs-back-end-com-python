# Manipulação de Arquivos em Python

# **Introdução à manipulação de arquivos**

Computadores lidam com dados armazenados em arquivos: textos, CSVs, logs, JSONs, imagens…
Python oferece ferramentas simples, mas poderosas, para criar, ler, escrever e gerenciar esses arquivos.

A função central para tudo isso é:

```python
open()
```

Ela abre um arquivo e retorna um **objeto de arquivo** — uma espécie de “ponte” entre o programa e o arquivo físico no disco.

---

# **Abrindo e fechando arquivos**

O padrão clássico:

```python
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()
```

Parâmetros importantes:

* `"r"` — leitura
* `"w"` — escrita (sobrescreve o arquivo)
* `"a"` — “append”, adiciona no fim
* `"r+"` — leitura + escrita sem apagar
* `"b"` — modo binário

Exemplo de modo binário:

```python
open("imagem.jpg", "rb")
```

### **Mas existe uma forma melhor…**

O Python recomenda usar **context manager (`with`)**, que fecha o arquivo automaticamente:

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
```

Esse bloco é seguro, limpo e não deixa arquivos abertos.

---

# **Lendo de um arquivo**

Depois de abrir o arquivo, você pode usar:

### **`read()` — lê tudo**

```python
with open("dados.txt", "r") as f:
    texto = f.read()
```

### **`readline()` — lê linha por linha**

```python
linha = f.readline()
```

### **`readlines()` — devolve lista de linhas**

```python
linhas = f.readlines()
```

### **For natural — iterar sobre o arquivo**

É eficiente e elegante:

```python
with open("dados.txt") as f:
    for linha in f:
        print(linha.strip())
```

Python trata o arquivo como um iterador.
Ótimo para arquivos grandes.

---

# **Escrevendo em um arquivo**

### **Sobrescrever (`w`)**

```python
with open("log.txt", "w") as f:
    f.write("Primeira linha\n")
```

`w` recria o arquivo do zero.

### **Adicionar no fim (`a`)**

```python
with open("log.txt", "a") as f:
    f.write("Nova entrada\n")
```

### **Escrever múltiplas linhas**

```python
linhas = ["linha 1\n", "linha 2\n"]

with open("multilinhas.txt", "w") as f:
    f.writelines(linhas)
```

---

# **Gerenciando arquivos e diretórios**

Python oferece módulos para manipular diretórios e arquivos do sistema.

### **`os` — para operações clássicas**

```python
import os

os.mkdir("pasta")               # criar pasta
os.listdir(".")                 # listar arquivos
os.remove("arquivo.txt")        # apagar arquivo
os.rename("velho.txt", "novo.txt")
```

### **`os.path` — trabalhar com caminhos**

```python
os.path.exists("arquivo.txt")
os.path.join("pasta", "arquivo.txt")
```

### **`shutil` — copiar, mover, remover recursivamente**

```python
import shutil

shutil.copy("a.txt", "b.txt")
shutil.move("a.txt", "pasta/a.txt")
shutil.rmtree("pasta")          # remove pasta inteira
```

### **`pathlib` — um jeito moderno e elegante**

```python
from pathlib import Path

p = Path("dados.txt")

if p.exists():
    print(p.read_text())
```

`pathlib` deixa o código mais limpo e orientado a objetos.

A biblioteca **`pathlib`** (a classe `Path`) é a forma moderna, limpa e elegante de manipular arquivos e diretórios em Python. Ela substitui quase tudo do módulo `os` e `os.path` com uma sintaxe mais legível, orientada a objetos e multiplataforma.

Quando você usa `Path`, o código deixa de parecer um amontoado de strings e começa a parecer uma conversa natural sobre caminhos.

---

# **Por que usar Path?**

* Manipulação de caminhos **sem concatenação manual**
* Operações intuitivas usando `/` no lugar de `os.path.join`
* Métodos poderosos para arquivos e diretórios
* Mais legível e seguro
* Melhor compatibilidade entre Windows, Linux e Mac

Python moderno recomenda `pathlib` para tudo relacionado a caminhos.
Abaixo estão equivalências entre `os.path` e `Path`, além de um guia elegante de uso.

---

# **Criando um caminho com Path**

Antes, no `os`:

```python
import os
caminho = os.path.join("pasta", "subpasta", "arquivo.txt")
```

Com Path:

```python
from pathlib import Path

caminho = Path("pasta") / "subpasta" / "arquivo.txt"
```

O operador `/` foi sobrecarregado para funcionar como um “join elegante”.

---

# **Obtendo o diretório atual**

Antes:

```python
os.getcwd()
```

Agora:

```python
Path.cwd()
```

---

# **Diretório do arquivo atual (**file**)**

Antes:

```python
os.path.dirname(os.path.abspath(__file__))
```

Agora:

```python
Path(__file__).resolve().parent
```

Muito mais semântico.

---

# **Nome do arquivo, extensão, pasta, stem**

Com `os.path` ficava feio.
Com `Path` é quase poesia:

```python
p = Path("pasta/relatorio.csv")

p.name        # 'relatorio.csv'
p.stem        # 'relatorio'
p.suffix      # '.csv'
p.parent      # Path('pasta')
```

Para extensões múltiplas (ex.: .tar.gz):

```python
p.suffixes    # ['.tar', '.gz']
```

---

# **Testando existência de arquivos**

Antes:

```python
os.path.exists("arquivo.txt")
```

Agora:

```python
p = Path("arquivo.txt")
p.exists()
```

Testar se é arquivo ou diretório:

```python
p.is_file()
p.is_dir()
```

---

# **Listar arquivos de um diretório**

Antes:

```python
for f in os.listdir("pasta"):
    print(f)
```

Com Path:

```python
for f in Path("pasta").iterdir():
    print(f)
```

Filtrar por extensão:

```python
for f in Path("pasta").glob("*.txt"):
    print(f)
```

Recursivo:

```python
for f in Path("pasta").rglob("*.py"):
    print(f)
```

---

# **Criar diretórios**

Antes:

```python
os.makedirs("nova_pasta", exist_ok=True)
```

Agora:

```python
Path("nova_pasta").mkdir(parents=True, exist_ok=True)
```

---

# **Criar, escrever e ler arquivos**

Antes (com `open`):

```python
with open("arquivo.txt", "w") as f:
    f.write("Olá")
```

Path simplifica:

```python
p = Path("arquivo.txt")
p.write_text("Olá", encoding="utf-8")
```

Ler:

```python
texto = p.read_text(encoding="utf-8")
```

Para binários:

```python
p.write_bytes(b"dados brutos")
dados = p.read_bytes()
```

Quando você usa **`Path.write_text()`**, **`Path.write_bytes()`**, **`Path.read_text()`** ou **`Path.read_bytes()`**, **não é necessário** usar um gerenciador de contexto — porque essas funções *internamente já abrem e fecham o arquivo* por conta própria.

Esses métodos são azulejos bem polidos do `pathlib`: eles existem justamente para dar **um atalho elegante e seguro** para leitura e escrita simples.

Mas isso não significa que o gerenciador de contexto deixou de ser importante.
Ele continua sendo necessário em cenários específicos, especialmente quando você precisa de **controle fino sobre leitura e escrita**.

---

# ✔ Quando **não** precisa usar `with open()`

Quando você usa os métodos simplificados do próprio `Path`:

```python
from pathlib import Path

p = Path("arquivo.txt")

# Escrever (sem with)
p.write_text("Olá, mundo!", encoding="utf-8")

# Ler (sem with)
conteudo = p.read_text(encoding="utf-8")
```

Esses métodos:

* abrem o arquivo,
* fazem a operação,
* **fecham automaticamente**,
* e te devolvem o resultado.

São perfeitos para:

* arquivos pequenos
* escrita rápida
* leitura simples
* operações que não precisam manipular linha a linha

O propósito deles é clareza e simplicidade.

---

# ✔ Quando **precisa** usar `with open()` mesmo com `Path`

Sempre que você precisa trabalhar com o arquivo **de forma mais granular**.

### 1. Leitura linha a linha

```python
with Path("dados.txt").open("r") as f:
    for linha in f:
        print(linha.strip())
```

### 2. Escrita incremental

```python
with Path("log.txt").open("a") as f:
    f.write("Nova entrada\n")
```

### 3. Trabalhar com arquivos grandes

`read_text()` lê tudo de uma vez — ótimo para arquivos pequenos, ruim para arquivos gigantes.

### 4. Especificar configurações detalhadas

* buffering
* newline controlada
* modo binário com operações contínuas
* escrita simultânea com flush manual

### 5. Usar métodos do próprio objeto arquivo

`seek()`, `tell()`, `writelines()`, etc.

---

# ✔ Comparando sintaxes

### Forma simples (não precisa de with)

```python
Path("arquivo.txt").write_text("Olá")
texto = Path("arquivo.txt").read_text()
```

### Forma detalhada (precisa de with)

```python
with Path("arquivo.txt").open("r", encoding="utf-8") as f:
    for linha in f:
        ...
```

Ambas são corretas.
A diferença é a **intenção**.

---

# ✔ Regra prática

Se sua ação for **instantânea** (ler ou escrever inteiro), use:
✔ `read_text()` / `write_text()`
✔ `read_bytes()` / `write_bytes()`

Se sua ação for **processual**, use:
✔ `with Path().open() as f:`

Ou seja:

* **Simples?** Path resolve tudo.
* **Complexo?** use `with open`.

---

# ✔ Exemplo real bem elegante

```python
from pathlib import Path

p = Path("relatorio.txt")

# Escrever título
p.write_text("Relatório de Vendas\n")

# Adicionar linhas depois
with p.open("a") as f:
    f.write("Item A: 10 unidades\n")
    f.write("Item B: 5 unidades\n")
```

Aqui você combina elegância + controle.

---

# 🎯 Conclusão

**Path não elimina o gerenciador de contexto — apenas elimina a necessidade dele em operações simples.**

Você ganha:

* métodos nativos e elegantes (`read_text`, `write_text`)
* capacidade total de usar `open()` quando precisar de controle

É o melhor dos dois mundos.

---

# **Mover, copiar e deletar arquivos**

Mover (antes com `shutil.move`):

```python
p.rename(novo_caminho)
```

Apagar:

```python
p.unlink()  # remove arquivo
```

Apagar diretório vazio:

```python
p.rmdir()
```

Para copiar, ainda precisa de `shutil`:

```python
import shutil
shutil.copy(p, destino)
```

Mas agora ambos podem ser `Path`.

---

# **Construção elegante de caminhos absolutos**

Absoluto:

```python
Path("arquivo.txt").resolve()
```

Unir caminho absoluto com arquivo filho:

```python
pasta = Path(__file__).resolve().parent
arquivo = pasta / "dados" / "log.txt"
```

Independente do SO.

---

# **Verificando partes do caminho**

```python
p = Path("/home/luciano/projetos/app/main.py")

p.parts
# ('/', 'home', 'luciano', 'projetos', 'app', 'main.py')
```

---

# **Leitura linha a linha usando Path**

```python
for linha in p.open():
    print(linha.strip())
```

Sim, `Path.open()` devolve um objeto de arquivo.

---

# **Exemplo completo: varrendo diretórios e processando arquivos**

```python
from pathlib import Path

pasta = Path("logs")

for arquivo in pasta.rglob("*.txt"):
    print(f"Lendo {arquivo.name}")
    conteudo = arquivo.read_text(encoding="utf-8")
    print(conteudo[:50], "...")
```

Só de ler isso já dá para sentir a diferença de clareza.

---

# **Quando usar os.path e quando usar Path?**

A verdade moderna:
👉 **Use Path para tudo**, exceto raras integrações com libs antigas.

`os.path` é legado.
`Path` é elegante, legível e mais seguro.

---

# **Se quiser, posso criar:**

* um **guia completo markdown** para seu README
* exercícios envolvendo `Path`
* comparativos diretos com `os.path`
* funções utilitárias reutilizáveis
* uma classe “FileManager” usando Path de forma profissional

Só escolher o próximo passo.

---

# **Tratamento de exceções em manipulação de arquivos**

Falhas acontecem: arquivo não existe, permissão negada, disco cheio…

Use `try/except` para tratar com elegância:

```python
try:
    with open("dados.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except PermissionError:
    print("Sem permissão para abrir esse arquivo.")
```

Erro genérico:

```python
except Exception as e:
    print("Erro inesperado:", e)
```

Exceções deixam o programa resiliente.

---

# **Boas práticas na manipulação de arquivos**

Algumas atitudes deixam tudo mais seguro e profissional:

### ✔ Sempre usar `with open()`

Fecha o arquivo automaticamente.

### ✔ Tratar exceções

Evita travamentos por problemas no sistema.

### ✔ Usar `pathlib` para caminhos

Mais legível e multiplataforma.

### ✔ Evitar ler arquivos gigantes com `read()`

Prefira leitura linha a linha.

### ✔ Sempre documentar encoding quando necessário

```python
open("dados.txt", encoding="utf-8")
```

### ✔ Evitar sobrescrever sem querer

Quando escrever, pense bem antes de usar `"w"`.

---

# **Trabalhando com arquivos CSV**

CSV é um dos formatos mais usados para dados tabulares.

Python tem o módulo nativo `csv`, simples e eficiente.

### **Lendo CSV**

```python
import csv

with open("dados.csv", newline="") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
```

### **Escrevendo CSV**

```python
import csv

with open("saida.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", 30])
```

### **Usando `DictReader` / `DictWriter`**

Ótimo para CSV com cabeçalho.

```python
import csv

with open("dados.csv") as f:
    leitor = csv.DictReader(f)
    for row in leitor:
        print(row["nome"], row["idade"])
```

### **Por que isso é útil?**

* manipular planilhas
* importar/exportar dados
* logs estruturados
* integração com sistemas simples

CSV é o "feijão com arroz" dos dados.

---

# **Amarrando tudo**

Manipulação de arquivos é um terreno essencial para qualquer desenvolvedor.
Ao dominar:

* abertura e fechamento
* leitura e escrita
* organização de diretórios
* tratamento de exceções
* boas práticas
* leitura de CSV

… você ganha autonomia para trabalhar com dados reais, scripts poderosos e integrações simples.
