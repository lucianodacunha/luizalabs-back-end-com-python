# **Dominando Funções em Python**

Funções são o mecanismo que transforma código em ideias reutilizáveis. Elas encapsulam comportamento, escondem detalhes, organizam raciocínio e permitem que um programa cresça sem virar um emaranhado de linhas soltas. Quando você domina funções, Python deixa de ser apenas uma linguagem e passa a ser uma forma clara de expressar pensamento.

Vamos caminhar pelos fundamentos com fluidez e precisão.

---

## **O que é uma função?**

Uma função é um bloco de código nomeado que executa uma tarefa específica.
Ela recebe valores (parâmetros), faz algum processamento e, muitas vezes, devolve um resultado.

A forma básica:

```python
def saudacao():
    print("Olá!")
```

E para usar:

```python
saudacao()
```

Sempre que você percebe que está repetindo lógica, ou que uma parte do código tem um propósito bem definido, isso é um convite para criar uma função.

---

## **Parâmetros: como uma função recebe informação**

Parâmetros são a porta de entrada.

```python
def saudacao_para(nome):
    print(f"Olá, {nome}!")
```

Você chama assim:

```python
saudacao_para("Luciano")
```

Python permite parâmetros simples, múltiplos e até bem flexíveis.

### **Parâmetros com valor padrão**

```python
def conectar(host="localhost", porta=3306):
    print(f"Conectando a {host}:{porta}")
```

Chamadas válidas:

```python
conectar()
conectar("servidor")
conectar(porta=8080)
```

Valores padrão tornam funções mais confortáveis e reduzem repetição.

---

## **Retorno: como uma função devolve resultados**

A palavra-chave `return` encerra a função e devolve um valor:

```python
def soma(a, b):
    return a + b
```

E você usa:

```python
resultado = soma(2, 3)
```

Uma função pode retornar vários valores — na verdade, retorna uma tupla:

```python
def estatisticas(lista):
    return min(lista), max(lista), sum(lista)
```

Uso:

```python
menor, maior, total = estatisticas([1, 2, 3])
```

Essas “múltiplas saídas” tornam o Python muito expressivo.

---

## **Argumentos posicionais e nomeados**

Python permite chamadas onde você escolhe a forma mais legível:

```python
def exibir(nome, idade):
    print(nome, idade)

exibir("Ana", 30)                 # posicional
exibir(nome="Ana", idade=30)      # nomeado
exibir(idade=30, nome="Ana")      # ordem livre com nomeados
```

Chamadas nomeadas aumentam a clareza quando a função tem muitos parâmetros.

---

## **Empacotamento e desempacotamento: `*args` e `**kwargs`**

Às vezes você quer funções flexíveis, que aceitem “quantos argumentos forem necessários”.

### **`*args` (posição variável)**

```python
def soma_variavel(*numeros):
    return sum(numeros)

soma_variavel(1, 2, 3)     # 6
```

`args` vira uma tupla com todos os argumentos posicionais recebidos.

### **`**kwargs` (nomeados variáveis)**

```python
def exibir_config(**opcoes):
    print(opcoes)

exibir_config(debug=True, verbose=False)
```

Isso vira um dicionário interno:

```python
{'debug': True, 'verbose': False}
```

É perfeito para funções que precisam ser extensíveis.

---

## **Escopo: onde uma variável existe**

Variáveis criadas dentro de uma função pertencem a ela:

```python
def teste():
    x = 10  # escopo local
```

Fora da função, `x` não existe.

Se quiser acessar uma variável externa, você pode, mas com cuidado.
Python resolve escopo seguindo a regra **LEGB** (Local, Enclosing, Global, Built-in):

1. Local
2. Enclosing (funções dentro de funções)
3. Global
4. Built-in

Isso mantém a organização e evita efeitos colaterais inesperados.

---

## **Funções como objetos**

Em Python, funções são cidadãos de primeira classe:

* podem ser armazenadas em variáveis
* passadas como argumento
* retornadas de outras funções
* colocadas em coleções

Exemplo:

```python
def dobro(x):
    return x * 2

operacao = dobro
operacao(5)     # 10
```

Isso abre portas para padrões como callbacks, funções de ordem superior e programação funcional.

---

## **Funções anônimas (lambdas)**

Quando a lógica é pequena, dá para criar funções rápidas:

```python
quadrado = lambda x: x * x
quadrado(4)  # 16
```

Usadas muito em:

* ordenação (`sorted(lista, key=lambda x: x.idade)`)
* filtros (`filter`, `map`)
* pequenas transformações

---

## **Documentação: o papel das docstrings**

Cada função pode ter uma descrição interna, acessível via `help()`:

```python
def dividir(a, b):
    """
    Divide a por b e retorna o resultado.
    Lança ZeroDivisionError se b for zero.
    """
    return a / b
```

Docstrings são ouro puro para clareza e manutenibilidade.


Na sequência, vamos explorar essas duas funcionalidades modernas da sintaxe de funções em Python — o **`/`** e o **`*` solitário. Essas duas notações existem para dar **clareza, controle e expressividade** na forma como parâmetros podem (ou devem) ser passados. É como se você tivesse uma pequena gramática dentro da assinatura da função.

---

# **Parâmetros posicionais com `/`**

O caractere **barra** (`/`) foi introduzido para permitir que você marque explicitamente parâmetros que **só podem ser passados por posição**, nunca por nome.

Isso existe por dois motivos principais:

1. desempenho e compatibilidade com funções internas (built-ins), que já usavam esse comportamento
2. deixar claro que certos parâmetros são conceitualmente posicionais (como coordenadas: `x, y`)

### **Sintaxe**

```python
def func(a, b, /, c, d):
    ...
```

Tudo antes do `/` é **posicional obrigatório**.
Tudo depois do `/` pode ser posicional **ou** nomeado.

### **Exemplo simples**

```python
def mover(x, y, /, velocidade=1):
    print(f"Movendo para ({x}, {y}) a {velocidade} m/s")
```

Uso correto:

```python
mover(10, 20)            
mover(10, 20, velocidade=2)
```

Uso incorreto (proibido):

```python
mover(x=10, y=20)   # erro
```

`x` e `y` devem ser posicionais.

### **Por que isso é útil?**

Para deixar claro que esses valores formam um *grupo conceitual*, e nomeá-los traz pouca clareza adicional.
Coordenadas, limites de intervalo, pares relacionados — tudo encaixa bem aqui.

---

# **Parâmetros nomeados obrigatórios com `*`**

Agora vamos ao outro lado da moeda.
O **asterisco solitário** (`*`) indica:

> “Daqui para frente, todos os parâmetros só podem ser passados por nome.”

É o oposto da barra.

### **Sintaxe**

```python
def func(a, b, *, c, d=0):
    ...
```

`a` e `b` podem ser posicionais.
Mas `c` e `d` **precisam** ser nomeados.

### **Exemplo prático**

```python
def criar_usuario(nome, idade, *, admin=False, ativo=True):
    print(nome, idade, admin, ativo)
```

Chamadas válidas:

```python
criar_usuario("Ana", 30)
criar_usuario("Ana", 30, admin=True)
criar_usuario("Ana", 30, ativo=False)
```

Chamadas inválidas:

```python
criar_usuario("Ana", 30, True, False)  # erro
```

Isso impede que parâmetros adicionais passem despercebidos.

### **Onde isso brilha?**

* APIs com muitos parâmetros opcionais
* funções com configurações ricas
* código que precisa evitar ambiguidades

É como obrigar o usuário da função a ser explícito.

---

# **Junção das duas ideias: `/` e `*` juntos**

Python permite declarar três tipos distintos de parâmetros:

* posicionais obrigatórios
* mistos (posicionais ou nomeados)
* nomeados obrigatórios

Tudo ao mesmo tempo:

```python
def func(a, b, /, c, d, *, e, f=0):
    print(a, b, c, d, e, f)
```

Interpretação:

* `a`, `b`: **somente posicionais**
* `c`, `d`: podem ser passados de qualquer forma
* `e`, `f`: **somente nomeados**

Uso correto:

```python
func(1, 2, 3, 4, e=5)
func(1, 2, c=3, d=4, e=5, f=9)
```

Uso incorreto:

```python
func(a=1, b=2, 3, 4, e=5)   # erro
func(1, 2, 3, 4, 5, 6)      # erro (e e f precisam ser nomeados)
```

---

# **Por que isso existe em Python?**

Esses recursos aparecem por necessidade de expressividade. Eles permitem que você:

* limite o uso indevido de parâmetros
* crie APIs claras e difíceis de usar errado
* dê pistas ao leitor do que é conceitualmente posicional
* force que parâmetros opcionais sempre sejam nomeados (melhorando leitura)

É um refinamento da linguagem que ajuda a tornar o código mais explícito — um valor central no Python.

---

# **Exemplo final com contexto real**

Imagine uma função para criar buffers em um projeto de geoprocessamento:

```python
def calcular_buffer(geometria, distancia, /, *, cap_style="round", join_style="round"):
    ...
```

Uso:

```python
calcular_buffer(gdf, 30)
calcular_buffer(gdf, 30, cap_style="square")
```

Não permitido:

```python
calcular_buffer(geometria=geom, distancia=30)  # erro
```

Por quê?

Porque `geometria` e `distancia` formam um par conceitualmente posicional.
E opções de estilo devem sempre ser nomeadas — pois são configurações.

---

## **Por que funções são tão importantes?**

* organizam o código em blocos cognitivos
* reduzem duplicação
* permitem testar cada parte isoladamente
* tornam programas expansíveis sem virar caos
* habilitam padrões mais sofisticados (decorators, closures, factories)

Funções são a ponte entre pensamento humano e execução computacional.
