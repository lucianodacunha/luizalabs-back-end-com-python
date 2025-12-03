# Aprendendo o Conceito de Herança com Python

## **O que é herança?**

Herança é um mecanismo onde **uma classe (classe filha)** herda atributos e métodos de **outra classe (classe pai/base)**.

A metáfora é direta:
uma *subclasse* herda características e comportamentos da *superclasse*.

Em Python, isso significa:

* reutilizar código
* especializar comportamentos
* evitar duplicações
* criar hierarquias lógicas

Por exemplo:

* `Animal` → classe base
* `Cachorro(Animal)` → herda tudo de Animal
* `Gato(Animal)` → idem

Você cria o geral na classe base e coloca o específico nas subclasses.

---

## **Sintaxe básica da herança**

```python
class ClassePai:
    ...

class ClasseFilha(ClassePai):
    ...
```

Simples, direto.

---

## **Exemplo inicial: Animal → Cachorro**

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico...")
```

Agora a subclasse:

```python
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
```

Uso:

```python
c = Cachorro("Rex")
c.emitir_som()  # Au au!
print(c.nome)   # Rex
```

Note que:

* `Cachorro` **não tem seu próprio construtor**, mas herdou `__init__` do `Animal`
* você pode sobrescrever métodos (como `emitir_som()`)

---

## **Chamando o construtor da classe pai**

Às vezes a subclasse precisa inicializar coisas extras.

Exemplo:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)   # chama o construtor da classe pai
        self.cargo = cargo
```

Uso:

```python
f = Funcionario("Ana", "Dev")
print(f.nome, f.cargo)
```

`super()` é a forma elegante e pythonica de chamar a implementação da classe pai.

---

## **Sobrescrita de métodos (override)**

A subclasse pode redefinir métodos da classe pai.

```python
class Veiculo:
    def mover(self):
        print("Veículo se movimentando...")

class Bicicleta(Veiculo):
    def mover(self):
        print("Pedalando...")
```

O Python automaticamente usa o método mais específico disponível:
se a subclasse sobrescreve → ela vence.

---

## **Herança múltipla em Python**

Python **permite** herança múltipla — uma classe pode herdar de várias classes.

Exemplo simples:

```python
class A:
    def fazer(self):
        print("A")

class B:
    def fazer(self):
        print("B")

class C(A, B):
    pass
```

```python
c = C()
c.fazer()  # "A" → porque A vem primeiro na lista de herança
```

O Python segue uma ordem chamada **MRO – Method Resolution Order**, que determina qual método vence quando várias classes têm implementações similares.

Herança múltipla é poderosa, mas exige cuidado para evitar “diamantes caóticos”.

---

## **Classe base abstrata (conceito avançado)**

Python permite criar classes que **não podem ser instanciadas**, apenas herdadas.
Isso é útil quando você quer definir contratos de comportamento.

Exemplo com `abc`:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
```

Agora qualquer subclasse é obrigada a implementar o método:

```python
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
```

Se não implementar, não compila.

---

## **Benefícios da herança**

* reduz repetição
* organiza código por hierarquias lógicas
* facilita especialização
* melhora reutilização
* aproxima conceitos do mundo real

Mas também traz riscos:

* excesso de herança cria sistemas rígidos
* mudanças na classe pai quebram várias subclasses
* herança múltipla pode gerar ambiguidade

Por isso existe outro conceito importante…

---

## **Herança vs Composição**

Regra prática comum:

> Prefira **composição** quando possível; use **herança** quando fizer sentido lógico.

Exemplo de composição:

```python
class Motor:
    def ligar(self):
        print("Motor ligado.")

class Carro:
    def __init__(self):
        self.motor = Motor()
```

Um carro *tem um* motor → composição.
Um cachorro *é um* animal → herança.

É uma diferença sutil, mas poderosa.

---

## **Exemplo completo: Conta Bancária com herança**

Classe base:

```python
class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
```

Subclasse:

```python
class ContaCorrente(Conta):
    def __init__(self, numero, saldo=0, limite=500):
        super().__init__(numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Limite insuficiente.")
```

Uso:

```python
cc = ContaCorrente(123, 100)
cc.sacar(300)
print(cc.saldo)
```

Aqui você vê:

* herança do construtor
* sobrescrita de método
* expansão de comportamento

Perfeito para entender OO aplicada.
