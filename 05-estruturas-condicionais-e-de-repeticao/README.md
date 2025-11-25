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

Estruturas condicionais e de repetição são o esqueleto do raciocínio em qualquer linguagem. Em Python, elas ganham uma fluidez quase narrativa — basta olhar a indentação e os dois-pontos para entender o que acontece. Vamos passear por elas com calma.

---

## **Condicionais: o programa aprendendo a decidir**

Uma condicional é uma encruzilhada do código. Você faz uma pergunta, e de acordo com a resposta, segue um caminho.

### **if — o guardião principal**

Ele testa uma condição e executa um bloco se ela for verdadeira.

```python
if idade >= 18:
    print("Entrada permitida")
```

O “`:`” abre o bloco.
A indentação diz o que pertence ao bloco.

### **elif — opções intermediárias**

Você encadeia hipóteses:

```python
if temperatura > 30:
    print("Quente")
elif temperatura > 20:
    print("Agradável")
else:
    print("Fresco")
```

Python avalia de cima para baixo e para no primeiro caso verdadeiro.
Esse padrão torna o raciocínio linear e direto.

### **else — o “se nada disso…”**

É a rede de segurança.
Se nenhuma condição anterior se encaixar, cai aqui.

---

## **Operador ternário — decisão compacta**

Para decisões curtas, Python tem uma forma expressiva:

```python
mensagem = "Adulto" if idade >= 18 else "Menor"
```

É útil para escolhas simples, não para lógicas complexas.

---

## **Repetições: o programa aprendendo a iterar**

Estruturas de repetição permitem que o código caminhe por coleções ou repita ações até que uma condição deixe de ser verdadeira.

---

## **for — o explorador de sequências**

O `for` em Python não é um contador automático; ele **itera sobre itens**.
Isso o aproxima mais de uma frase: “para cada coisa no conjunto…”

```python
for fruta in ["maçã", "pera", "uva"]:
    print(fruta)
```

Você pode percorrer strings:

```python
for letra in "python":
    print(letra)
```

Ou usar `range()` quando precisa de uma sequência numérica:

```python
for i in range(5):   # 0, 1, 2, 3, 4
    print(i)
```

Se quiser começar por outro número:

```python
range(2, 6)  # 2, 3, 4, 5
```

Ou ainda controlar o passo:

```python
range(0, 10, 2)  # 0, 2, 4, 6, 8
```

O `for` é a estrela do Python: legível, previsível e poderoso.

---

## **while — o laço condicionado**

O `while` gira enquanto a condição for verdadeira.

```python
contador = 0

while contador < 3:
    print("Rodando...")
    contador += 1
```

É ótimo para situações em que o número de repetições não é conhecido de antemão — loops que dependem de eventos, sensores, entrada do usuário, etc.

Mas cuidado: se a condição nunca mudar, vira loop infinito.

---

## **Interrupções de laço**

O Python te dá três ferramentas que ajudam o fluxo dentro de loops.

### **break — sai do loop imediatamente**

```python
for n in range(10):
    if n == 5:
        break
    print(n)
```

Quando `n == 5`, o loop acaba — como puxar o freio de mão.

### **continue — pula para a próxima iteração**

```python
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)  # só números ímpares
```

Ele interrompe só o ciclo atual do loop, não o loop inteiro.

### **else em loops — o detalhe elegante**

Pouca gente usa, mas ele existe:

```python
for n in range(5):
    if n == 10:
        break
else:
    print("O número 10 não apareceu")
```

O bloco `else` só é executado se o loop **não** encontrar um `break`.

É quase uma frase lógica: “se percorri tudo sem parar, então…”

---

## **Compreensões de lista (bonus evolutivo)**

Se o Python tivesse uma assinatura musical, seria isso:

```python
quadrados = [x**2 for x in range(6)]
```

É uma forma compacta de expressar um loop de transformação.
Quando você dominar condicionais e loops tradicionais, compreensões vão abrir uma porta para soluções concisas e elegantes.

---

## **Costurando tudo**

As estruturas condicionais permitem escolher caminhos.
Os loops permitem repetir caminhos.
E a indentação coloca tudo em camadas visuais que guiam o olhar.

Quando você entende esse trio — decisão, repetição e estrutura — começa a sentir o Python como uma história que se desenrola, linha após linha.
