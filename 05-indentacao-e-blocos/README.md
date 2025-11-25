# Indentação e blocos

Indentação e blocos são onde o Python revela sua personalidade. Ele não usa chaves, não usa “begin/end”, não usa palavras mágicas para abrir ou fechar estruturas. Ele usa **espaço** — literalmente — como parte da sintaxe. Essa escolha deixa o código com aparência limpa, mas também exige que você trate indentação como parte da gramática, não como decoração.


---

## **Indentação: o espaço que significa algo**

Em Python, **indentação não é estética — é estrutura**.
Quatro espaços dizem ao interpretador: *“isso aqui pertence ao bloco acima”*.
Sem eles, não há bloco; com eles no lugar errado, o bloco é outro.

O clássico:

```python
if idade >= 18:
    print("Pode entrar")
```

Aqui, a indentação define o escopo do `print`.
Se você tirar os quatro espaços, a linha sai do bloco:

```python
if idade >= 18:
print("Pode entrar")   # Erro de sintaxe
```

O interpretador reclama, porque o Python lê indentação como se fossem pontuações invisíveis.

---

## **Por que 4 espaços?**

Porque o PEP 8 recomenda, e virou consenso.
Tabs? Melhor evitar. Misturar tab com espaço é uma receita para erros invisíveis, especialmente quando o arquivo vai para um repositório ou passa por editores diferentes.

Configure seu editor (VSCode faz isso por padrão):

* “Insert Spaces”: `true`
* “Tab Size”: `4`

E você nunca mais pensa nisso.

---

## **Blocos: quando o Python entende que algo começa e termina**

Um bloco é aberto sempre que uma linha termina com `:`.
Esse `:` é a bandeirinha que diz: *“prepare-se, vem um bloco aí”*.

Você encontra isso em:

* `if`, `elif`, `else`
* `for`
* `while`
* `try`, `except`, `finally`
* `def`
* `class`
* context managers (`with`)

Exemplo com vários blocos aninhados:

```python
def processar(lista):
    for item in lista:
        if item % 2 == 0:
            print(f"{item} é par")
        else:
            print(f"{item} é ímpar")
```

A indentação cria camadas — visualmente e semanticamente.

---

## **O bloco acompanha o recuo**

Quando você remove a indentação, muda o escopo de execução:

```python
for n in range(3):
    print("Dentro do loop")
print("Fora do loop")
```

Mentalmente:

* uma linha indentada → pertence ao “mundo do loop”
* sem indentação → mundo externo

É quase físico: o código se afasta e se aproxima para indicar hierarquia.

---

## **Indentação profunda: como manter legível**

Blocos dentro de blocos dentro de blocos podem virar uma espiral descendente.
Mas Python te dá maneiras suaves de cortar profundidade:

### 1. Usar `return` cedo

```python
def validar(x):
    if x < 0:
        return False
    if x > 100:
        return False
    return True
```

Evite:

```python
def validar(x):
    if x >= 0:
        if x <= 100:
            return True
        else:
            return False
    else:
        return False
```

O Python gosta de estruturas horizontais, não verticais.

### 2. Quebrar trechos em funções menores

Quando a indentação começa a virar “escada”, é hora de dar nome a algumas partes.

---

## **Um detalhe interessante: parênteses anulam indentação obrigatória**

Dentro de `()`, `[]` ou `{}`, você pode quebrar a linha sem precisar do “\”.

```python
resultado = (
    valor_inicial
    + taxa
    - desconto
)
```

O interpretador entende que esse bloco lógico continua, mesmo sem indentação específica.

Esse truque deixa chamadas longas respirarem.

---

## **Erros comuns para ficar atento**

• Indentar com 2 espaços em um ponto e 4 em outro
• Misturar tab e espaço
• Esquecer o `:` depois de um `if`, `for` etc.
• Colocar indentação demais (acidental) e criar um bloco sem querer:

```python
if condicao:
        print("Isso cria um bloco extra")
```

Python não briga com você, mas cria a estrutura exatamente como você escreveu — e aí o comportamento pode surpreender.

---

## **A beleza disso tudo**

O código Python ganha leitura quase tipográfica.
Os blocos parecem parágrafos.
A indentação conduz o olhar.
Você percebe que programar é também uma questão de layout.

E, quando internaliza isso, o fluxo de leitura se torna natural — quase como se o cérebro entendesse os blocos antes mesmo de ler as palavras.
