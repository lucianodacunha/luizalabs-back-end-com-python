# Interfaces e Classes Abstratas com Python

## 1. Variáveis de classe vs variáveis de instância

### Variável de instância

Pertence **a cada objeto**.

```python
class Conta:
    def __init__(self, numero):
        self.numero = numero      # instância
        self.saldo = 0            # instância
```

Cada `Conta` tem seu `saldo` e `numero`.

```python
c1 = Conta(1)
c2 = Conta(2)
c1.saldo = 100
print(c2.saldo)  # 0
```

### Variável de classe

Pertence **à classe inteira**, compartilhada por todas as instâncias.

```python
class Conta:
    taxa_juros = 0.01  # variável de classe

    def __init__(self, numero):
        self.numero = numero
```

Uso:

```python
Conta.taxa_juros       # preferível
c = Conta(1)
c.taxa_juros           # funciona, mas é a mesma da classe
```

Se você fizer:

```python
c.taxa_juros = 0.02
```

Você criou **um atributo de instância** com o mesmo nome, que “sombra” o da classe. A variável de classe continua existindo em `Conta.taxa_juros`.

Regra mental:

* **Característica comum a todas as instâncias?** → variável de classe.
* **Estado específico de cada objeto?** → variável de instância.

---

## 2. Métodos de classe e métodos estáticos

Além de métodos “normais” (de instância), Python tem:

* `@classmethod`
* `@staticmethod`

### Métodos de instância (os “normais”)

Recebem `self` (a instância) como primeiro parâmetro:

```python
class Conta:
    def __init__(self, numero):
        self.numero = numero

    def exibir(self):
        print(f"Conta {self.numero}")
```

Chamados assim:

```python
c = Conta(1)
c.exibir()
```

### `@classmethod`

Recebe a **classe (`cls`)** como primeiro parâmetro, não a instância.

```python
class Usuario:
    dominio_email = "exemplo.com"

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @classmethod
    def com_email_padrao(cls, nome):
        email = f"{nome.lower()}@{cls.dominio_email}"
        return cls(nome, email)
```

Uso:

```python
u = Usuario.com_email_padrao("Luciano")
print(u.email)  # "luciano@exemplo.com"
```

Para que serve?

* *Factories* (construtores alternativos)
* Acessar/usar variáveis de classe
* Criar instâncias de forma mais semântica

### `@staticmethod`

Não recebe nem `self` nem `cls`. É só uma função dentro da classe, por organização.

```python
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
```

Uso:

```python
Matematica.somar(2, 3)   # 5
```

Poderia ser uma função solta? Poderia.
Mas às vezes faz sentido agrupar por contexto.

Regra prática:

* Precisa da instância? → método normal
* Precisa só da classe? → `@classmethod`
* Não precisa de nenhum dos dois, mas é conceitualmente da classe? → `@staticmethod`

---

## 3. O que são interfaces? (jeito Python de pensar)

Python não tem palavra-chave `interface` (como Java), mas o **conceito** existe:
interface é um **contrato de métodos** que uma classe se compromete a implementar.

Em Python, isso aparece de três formas principais:

### a) Duck typing (interface implícita)

Se um objeto:

* tem método `voar()`
* e você precisa de algo que “voe”

Você não exige que ele herde de `Voador`. Você simplesmente chama:

```python
def fazer_voar(obj):
    obj.voar()
```

Se tem `voar`, serve.
Isso é **interface por comportamento** e é super pythonico.

### b) ABCs (Abstract Base Classes)

A forma “formal” de interface em Python, via `abc`.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
```

Qualquer classe que herdar de `Forma` precisa implementar `area()`.

### c) Protocols (do módulo `typing`, Python 3.8+)

Mais avançado, usado pra tipagem estática:

```python
from typing import Protocol

class Voador(Protocol):
    def voar(self) -> None:
        ...
```

Qualquer classe que implemente `voar()` é “aceita” como `Voador`, mesmo sem herança.

---

## 4. Classes abstratas

Classes abstratas são classes que:

* **não devem ser instanciadas diretamente**
* servem como base para outras classes
* definem **contratos de comportamento**

Via `abc`:

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, velocidade):
        self.velocidade = velocidade

    @abstractmethod
    def mover(self):
        pass
```

Subclasses:

```python
class Carro(Veiculo):
    def mover(self):
        print(f"Carro se movendo a {self.velocidade} km/h")

class Bicicleta(Veiculo):
    def mover(self):
        print(f"Bicicleta pedalando a {self.velocidade} km/h")
```

Tentativa de instanciar `Veiculo()` → erro.
Instanciar `Carro` e `Bicicleta` funciona.

Classes abstratas são **interfaces com músculos**:
têm contratos (`@abstractmethod`) e podem ter implementação parcial (métodos concretos).

---

## 5. Ponto extra importante: *mixins*

Mixins são classes pensadas **só** para adicionar comportamento, não para existir sozinhas.

Exemplo:

```python
class LogMixin:
    def log(self, mensagem):
        print(f"[LOG] {mensagem}")
```

Usando com herança múltipla:

```python
class Servico(LogMixin):
    def executar(self):
        self.log("Executando serviço...")
```

`LogMixin` é quase uma “interface com implementação”:
não faz sentido como objeto, mas é ótimo como **componente reutilizável**.

---

## 6. Amarrando tudo

Você agora tem um mapa mais completo:

* **Variáveis de classe** → estado compartilhado
* **Variáveis de instância** → estado individual
* **Métodos de instância** → usam `self`, dependem do objeto
* **Métodos de classe** → usam `cls`, criam/operam na classe
* **Métodos estáticos** → funções organizadas dentro da classe
* **Interfaces** → contratos de comportamento (implícitos via duck typing ou explícitos via ABC/Protocol)
* **Classes abstratas** → bases que definem o que as filhas DEVEM implementar
* **Mixins** → classes auxiliares para compartilhar comportamento

Isso tudo junto te dá ferramentas pra desenhar APIs orientadas a objetos com clareza, extensibilidade e menos gambiarra.
