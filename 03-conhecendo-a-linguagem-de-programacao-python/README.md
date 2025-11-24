# Conhecendo a linguagem de programação Python

Vamos passear por esses fundamentos com leveza, mas sem perder a profundidade — Python tem uma graça especial quando você percebe que tudo nele é coerente e mais simples do que parece à primeira vista.

---

## **1 — Tipos de dados**

Python trata tipos como identidades flexíveis. Você não declara, apenas **usa** — e o tipo emerge do valor.

Tipos básicos mais comuns:

**Inteiros (`int`)**
Números inteiros, sem limite de tamanho além da memória disponível.

```python
idade = 34
```

**Ponto flutuante (`float`)**
Números reais.

```python
preco = 19.99
```

**Booleanos (`bool`)**
Os filósofos da computação: `True` e `False`.

```python
ativo = True
```

**Strings (`str`)**
Texto. Imutáveis (como papel já impresso).

```python
nome = "Luciano"
```

**Listas (`list`)**
Coleções mutáveis, ordenadas.

```python
frutas = ["maçã", "pera", "uva"]
```

**Tuplas (`tuple`)**
Coleções ordenadas, porém imutáveis.

```python
coordenada = (21.8, -47.2)
```

**Dicionários (`dict`)**
Pares chave-valor.

```python
usuario = {"nome": "Luciano", "idade": 34}
```

**Conjuntos (`set`)**
Coleções sem ordem, sem elementos repetidos.

```python
cidades = {"SP", "RJ", "BH"}
```

Python tem outros (complexos, bytes, intervalo etc.), mas esses formam o *vocabulário básico*.

---

## **2 — O modo interativo**

O modo interativo é o playground embutido do Python.
Você entra nele simplesmente digitando:

```bash
python
```

Ou com um toque mais moderno:

```bash
python3
```

E aparece o famoso `>>>`.
Qualquer expressão digitada ali é avaliada imediatamente.

Por que isso é útil?

• testar ideias
• experimentar APIs
• validar comportamentos estranhos
• aprender “tateando”

Exemplo no console:

```python
>>> 10 * 3
30
>>> type(10 * 3)
<class 'int'>
```

Tem também:

• **IPython**, mais poderoso, com cores e auto-complete
• **Notebooks (Jupyter)**, que viraram o laboratório padrão para ciência de dados

O modo interativo é o quintal onde você experimenta antes de escrever código formal.

---

## **3 — Variáveis e constantes**

Python não tem constantes “verdadeiras” como outras linguagens.
Ele confia em você — é quase um pacto de cavalheiros.

### Variáveis

São nomes que apontam para valores:

```python
nome = "Luciano"
idade = 34
```

Por baixo, uma variável é apenas uma etiqueta para um objeto na memória.

### “Constantes” (aspas garantidas)

A convenção é usar **MAIÚSCULAS**:

```python
TAXA_DE_JUROS = 0.13
```

Não impede alteração, mas indica: *por favor, não toque nisso*.

### Nomeação sensata

Python segue snake_case:

```python
nome_completo = "Ada Lovelace"
```

O código fica narrativo e fácil de ler.

---

## **4 — Conversão de tipos**

Python permite converter tipos explicitamente.
Isso evita confusões quando você mistura números, strings e dados de entrada.

Conversões mais comuns:

```python
int("10")          # 10
float("3.14")      # 3.14
str(123)           # "123"
bool(0)            # False
bool(1)            # True
```

Útil quando dados vêm de entrada do usuário:

```python
idade = int(input("Digite sua idade: "))
```

Também funciona em coleções:

```python
list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']
tuple([1, 2, 3])   # (1, 2, 3)
set("banana")      # {'b', 'a', 'n'}
```

O ponto é: conversão explícita evita ambiguidades.

---

## **5 — Funções de entrada e saída de dados**

Python trata entrada e saída de forma direta, mas cheia de nuances interessantes.

### **Saída: `print()`**

É o mensageiro universal:

```python
print("Olá, mundo!")
```

Tem flexibilidade:

```python
print("A soma é", 2 + 3)
print("Linha 1", end=" | ")
print("Linha 2")
```

Formatar valores fica mais elegante com f-strings:

```python
nome = "Luciano"
idade = 34
print(f"{nome} tem {idade} anos")
```

Isso virou padrão moderno — ágil e limpo.

---

### **Entrada: `input()`**

Tudo que vem de `input()` chega como **string**:

```python
valor = input("Digite algo: ")
```

Se quiser número, converta:

```python
preco = float(input("Digite o preço: "))
```

UM detalhe que pega muitos iniciantes:

```python
input()  # sempre string
```

Ou seja, se digitar 10, o valor é `"10"`, não 10.

---

## Amarrando as ideias

Tipos representam a natureza dos dados.
O modo interativo permite explorar essas naturezas ao vivo.
Variáveis nomeiam intenções.
Conversão de tipos permite conciliar mundos diferentes.
Entrada e saída são as portas da conversa entre você e o programa.
