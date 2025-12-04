# Conhecendo Polimorfismo em Python

## **O que é polimorfismo?**

A palavra vem do grego: *poli* (muitas) + *morphé* (formas).
No contexto da programação:

> **Polimorfismo é a capacidade de diferentes objetos compartilharem a mesma interface, mas fornecerem implementações específicas.**

Ou, dito de forma mais leve:

> “Vários objetos falam o mesmo idioma, mas cada um tem seu sotaque.”

O importante não é *o tipo* do objeto, mas se ele **sabe responder** ao método que você está chamando.

---

## **Polimorfismo e Herança**

O caminho mais comum para o polimorfismo surgir é via **herança**.

Pense em uma classe base:

```python
class Animal:
    def emitir_som(self):
        print("Som genérico...")
```

E subclasses especializadas:

```python
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
```

Agora, se você colocar vários animais em uma lista:

```python
animais = [Cachorro(), Gato(), Animal()]
```

E fizer:

```python
for animal in animais:
    animal.emitir_som()
```

A saída será:

```
Au au!
Miau!
Som genérico...
```

Isso é polimorfismo:
**o mesmo método → comportamentos diferentes**, dependendo do tipo do objeto.

---

## **Polimorfismo não depende exclusivamente de herança**

Em Python, isso é ainda mais interessante porque a linguagem segue o princípio do *duck typing*:

> “Se parece um pato, nada como um pato e grasna como um pato… é um pato.”

Ou seja:
Se um objeto implementa o método necessário, ele pode ser usado, mesmo que não tenha relação de herança com ninguém.

Exemplo:

```python
class Carro:
    def mover(self):
        print("Dirigindo...")

class Bicicleta:
    def mover(self):
        print("Pedalando...")

class Barco:
    def mover(self):
        print("Navegando...")
```

Agora:

```python
veiculos = [Carro(), Bicicleta(), Barco()]

for v in veiculos:
    v.mover()
```

Funcionará perfeitamente.

Não existe uma superclasse “Veiculo”.
O polimorfismo acontece **pela interface** — todos eles possuem o método `mover()`.

Essa flexibilidade é uma das belezas de Python.

---

## **Polimorfismo + Classes Abstratas (contratos formais)**

Se você quiser algo mais controlado — um contrato obrigatório — Python também fornece isso via `abc`:

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
```

Subclasses agora **são obrigadas** a implementar:

```python
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
```

Assim, você garante polimorfismo com relação à área:

```python
formas = [Quadrado(4), Quadrado(10)]

for f in formas:
    print(f.area())
```

Cada uma calcula a área à sua maneira — mas a interface é a mesma.

---

## **Onde o polimorfismo brilha?**

O polimorfismo é útil quando você quer:

#### **1. Escrever código genérico**

Funções que trabalham com vários tipos diferentes, mas que seguem a mesma “assinatura” de métodos.

#### **2. Extensibilidade**

Adicionar novos comportamentos sem alterar código já existente.

#### **3. Substituição**

Qualquer objeto filho pode substituir o pai sem quebrar o programa (Princípio de Substituição de Liskov — LSP).

#### **4. Organização natural**

Se você cria um conjunto de classes relacionadas, o polimorfismo permite trabalhar com todas elas como se fossem uma só “família comportamental”.

---

## **Polimorfismo não é sobre “tipos”, é sobre “comportamento”**

Num código polimórfico bem escrito, você raramente pergunta:

```python
if isinstance(obj, Cachorro):
```

Em vez disso, você simplesmente confia:

```python
obj.emitir_som()
```

E deixa o objeto decidir *como* responder.

Polimorfismo é confiar na interface, não na classe.

---

## **Um exemplo mais rico: pagamentos**

```python
class Pagamento:
    def pagar(self, valor):
        raise NotImplementedError()
```

Subclasses:

```python
class CartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"Pagando {valor} com cartão de crédito.")

class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Gerando boleto de R${valor}.")
```

Uso:

```python
def processar_pagamento(pagamento, valor):
    pagamento.pagar(valor)
```

Agora:

```python
processar_pagamento(CartaoCredito(), 100)
processar_pagamento(Boleto(), 250)
```

Essa função funciona com qualquer método de pagamento — presente ou futuro.

Isso é polimorfismo elevando o design do código.

---

## **Resumo da história**

Polimorfismo é:

* Objetos diferentes
* Compartilhando a mesma interface
* Respondendo do seu jeito
* Permutáveis entre si
* Independentes de tipo (em Python)
* Fortalecidos pela herança, mas não dependentes dela

É o que permite:

* funções flexíveis
* código genérico
* extensibilidade
* design clean e natural

Sem polimorfismo, OO seria apenas um jeito organizado de juntar funções.
Com ele, OO vira um sistema vivo, expressivo e expansível.

# Outras observações sobre polimorfismo

# ✅ **Polimorfismo NÃO é sobrecarga de métodos**

Embora os dois termos existam no universo da orientação a objetos, eles tratam de **ideias diferentes**.

---

# 🎭 **O que é polimorfismo?**

Polimorfismo é a capacidade de **mesmo método** (mesmo nome) ter **comportamentos diferentes** dependendo **do objeto que o executa**.

Exemplo:

```python
class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
```

E ao chamar:

```python
for animal in (Cachorro(), Gato()):
    animal.emitir_som()
```

Cada objeto responde do **seu jeito**, mesmo com **o mesmo método**.

👉 Isso é **polimorfismo por sobrescrita** (override), comum em Python e outras linguagens OO.

---

# 🔁 **O que é sobrecarga de métodos?**

Sobrecarga significa **métodos com o mesmo nome, mas assinaturas diferentes**, como em Java ou C++:

```java
int soma(int a, int b)
int soma(int a, int b, int c)
```

Python **não suporta sobrecarga de métodos nativamente**.
A última definição sobrescreve a anterior:

```python
class Calc:
    def soma(self, a, b):
        return a + b

    def soma(self, a, b, c):
        return a + b + c
```

Agora `soma(a, b)` **não existe mais** — só vale a versão com 3 parâmetros.

Se você quiser simular sobrecarga, precisa usar:

* argumentos opcionais (`*args`)
* valores padrão
* verificações internas

Exemplo em Python:

```python
class Calc:
    def soma(self, *valores):
        return sum(valores)
```

Não é sobrecarga real — é apenas flexibilidade.

---

# 🔥 **Então qual a relação entre polimorfismo e sobrecarga?**

### ✔ Em linguagens como Java e C++, ambos existem:

* **Sobrecarga** → escolher versões diferentes do *mesmo método* com base nos parâmetros
* **Polimorfismo** → escolher a implementação certa com base no *tipo do objeto*

### ✔ Em Python, sobrecarga formal **não existe**

Mas polimorfismo existe de forma **forte** e muito natural.

Em Python:

* **polimorfismo** = sobrescrever métodos em subclasses **ou** duck typing
* **sobrecarga** = simulada com parâmetros opcionais, não nativa

---

# 🦆 **Bonus: Polimorfismo sem herança — Duck Typing**

Python não exige herança para polimorfismo:

```python
class Pato:
    def fazer_som(self):
        print("Quack")

class Humano:
    def fazer_som(self):
        print("Oi!")

def executar_som(obj):
    obj.fazer_som()  # polimorfismo por interface

executar_som(Pato())
executar_som(Humano())
```

Se algo **se comporta** como um pato, é um pato.
Esse é o polimorfismo mais natural de Python.

---

# 🎯 **Resumo épico para fixar**

| Conceito                   | Python suporta?   | O que é                                            |
| -------------------------- | ----------------- | -------------------------------------------------- |
| **Sobrescrita (override)** | ✔ Sim             | Subclasse redefine método da classe pai            |
| **Polimorfismo**           | ✔ Sim             | Mesmo método, implementações diferentes por objeto |
| **Sobrecarga (overload)**  | ❌ Não nativamente | Métodos com mesmo nome e assinaturas diferentes    |

👉 **Um método polimórfico geralmente é um método sobrescrito**,
mas **não é um método sobrecarregado** — são conceitos diferentes.
