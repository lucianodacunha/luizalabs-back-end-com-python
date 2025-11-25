# Manipulando String com Python 

Strings são quase pequenos universos em Python. Elas guardam texto, claro, mas também funcionam como sequências altamente manipuláveis. A linguagem trata texto com tanto carinho que trabalhar com ele fica natural — quase como brincar com argila sintática.

---

## **Métodos úteis da classe `str`**

A classe `str` vem com um arsenal pronto. Não precisa decorar — basta saber que existe e reconhecer pelo nome.

### **Transformações de caixa**

```python
s = "Python"
s.lower()    # "python"
s.upper()    # "PYTHON"
s.title()    # "Python"
s.capitalize()  # "Python"
```

### **Remoção de espaços**

```python
"  texto  ".strip()   # remove nas duas pontas
"  texto  ".lstrip()  # remove à esquerda
"  texto  ".rstrip()  # remove à direita
```

### **Substituição**

```python
"banana".replace("a", "@")   # "b@n@n@"
```

### **Dividir e juntar**

```python
"nome,sobrenome".split(",")   # ["nome", "sobrenome"]

"-".join(["2025", "11", "24"])  # "2025-11-24"
```

### **Busca**

```python
"python".startswith("py")   # True
"python".endswith("on")     # True
"python".find("th")         # 2 (posição)
"python".count("o")         # 1
```

### **Teste de tipo textual**

```python
"123".isdigit()
"abc".isalpha()
"abc123".isalnum()
```

Esses métodos fazem 90% das tarefas cotidianas com texto.

---

## **Interpolação de variáveis**

A maneira moderna e elegante de inserir variáveis dentro de strings é a **f-string**.

```python
nome = "Luciano"
idade = 34

texto = f"{nome} tem {idade} anos"
```

Formatar valores é fácil:

```python
pi = 3.14159
f"O valor é {pi:.2f}"     # "O valor é 3.14"
```

F-strings também aceitam expressões:

```python
f"A soma é {2 + 3}"
```

Outras formas existem, mas hoje são menos usadas:

• `"{} tem {}".format(nome, idade)`
• `"%" % valores` (estilo C — antiquado)

F-strings ganharam a guerra pela clareza.

---

## **Fatiamento de string**

Strings são sequências — cada caractere tem um índice.
Python usa a notação de fatiamento `s[início:fim:passo]`.

```python
s = "Python"
```

### **Índices positivos**

```python
s[0]    # 'P'
s[1]    # 'y'
```

### **Índices negativos**

Eles contam de trás pra frente:

```python
s[-1]   # 'n'
s[-2]   # 'o'
```

### **Fatiamento básico**

```python
s[0:3]      # "Pyt"
s[2:6]      # "thon"
s[:4]       # "Pyth"  (omitir início = do começo)
s[3:]       # "hon"   (omitir fim = até o final)
```

### **Fatiamento com passo**

```python
s[::2]      # "Pto"  (pula de 2 em 2)
s[::-1]     # "nohtyP"  (string invertida!)
```

Esse último virou quase um símbolo da comunidade — maneira canônica de inverter texto.

---

## **String de múltiplas linhas**

Python usa aspas triplas para criar blocos de texto.

```python
texto = """
Linha 1
Linha 2
Linha 3
"""
```

Elas preservam quebras de linha e espaços literalmente.
Úteis para:

• textos longos
• SQL embutido
• HTML embutido
• docstrings de funções e classes

Exemplo de docstring:

```python
def saudar(nome):
    """
    Retorna uma saudação amigável.
    Ideal para iniciar conversas com humanos ou robôs.
    """
    return f"Olá, {nome}!"
```

A string triplamente aspada vira parte da documentação da função.

---

## **Amarrando tudo**

Strings são sequências maleáveis.
Métodos dão ferramentas para transformar texto.
Interpolação permite encaixar valores como peças de Lego.
Fatiamento oferece controle fino sobre pedaços da string.
E strings multilinha deixam textos extensos mais naturais.

Quando você domina esses quatro blocos, começa a sentir que texto deixa de ser um obstáculo e passa a ser uma ferramenta sofisticada — algo essencial em qualquer atividade que envolve análise de dados, arquivos, logs, APIs, web e até geoprocessamento.
