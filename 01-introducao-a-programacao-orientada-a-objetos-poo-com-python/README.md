# Introdução à Programação Orientada a Objetos (POO) com Python

# **O que é Orientação a Objetos?**

Orientação a Objetos (OO) é um **paradigma de programação** que organiza o software em torno de **entidades** chamadas *objetos*.
Esses objetos:

* representam algo concreto ou abstrato
* carregam dados
* possuem comportamentos
* se relacionam com outros objetos

A grande sacada da OO é **modelar problemas do mundo real usando estruturas de código que parecem “coisas” ao invés de “funções soltas”**.

Uma classe pode representar:

* um cliente
* um pedido
* uma conta bancária
* uma coordenada geográfica
* um sensor
* um usuário de API

E cada objeto é uma **instância real** dessa ideia.

OO ajuda a:

* organizar código
* reduzir repetição
* facilitar manutenção
* permitir extensões sem quebrar o mundo
* aproximar o raciocínio humano do raciocínio computacional

É um estilo de pensar, mais do que uma sintaxe.

---

# **Classes e Objetos: o coração da OO**

## **Classe**

Uma classe é um *molde*, *modelo*, uma *fábrica de objetos*.

É a definição conceitual:

> “como deve ser um objeto deste tipo?”

Por exemplo, classe `Carro` pode definir:

* atributos: cor, marca, velocidade
* métodos: acelerar(), frear(), buzinar()

## **Objeto**

Um objeto é uma **instância concreta** da classe.

Se a classe é o “molde”, o objeto é o “produto”.

A classe “Carro” é abstrata.
Mas um carro azul, placa XYZ-1234, que acelera e buzina, é um **objeto real**.

No Python:

* classe → blueprint
* objeto → instância criada a partir desse blueprint

Essa distinção é fundamental para OO fazer sentido.

---

# **Criando seu primeiro programa em OO**

Vamos começar simples, com uma classe representando uma Conta Bancária.

### **Classe**

```python
class Conta:
    pass
```

Essa classe não faz nada ainda, mas já existe.

### **Criando um objeto**

```python
c1 = Conta()
print(c1)
```

Você acabou de criar uma instância real de Conta.

### Vamos dar vida à classe

Adicionando atributos e métodos:

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
```

Agora veja os objetos funcionando:

```python
c1 = Conta("Luciano", 100)
c1.depositar(50)
c1.sacar(30)
print(c1.saldo)  # 120
```

De repente, a ideia de “conta bancária” virou um **objeto vivo** no código.

---

# **Construtores e Destrutores**

Essas são duas engrenagens internas importantes para o ciclo de vida dos objetos.

## **Construtor (`__init__`)**

O construtor é chamado automaticamente **toda vez que um objeto é criado**.

No Python, ele se chama:

```python
def __init__(self, ...):
```

Ele serve para:

* inicializar atributos
* validar dados
* preparar o objeto para uso

Exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

Criar um objeto:

```python
p = Pessoa("Ana", 30)
```

O Python automaticamente chama `__init__`.

### Importante:

O método real que cria o objeto é `__new__`, mas quase nunca você precisa lidar com ele.

---

## **Destrutor (`__del__`)**

O destrutor é chamado quando o objeto está prestes a ser destruído.
Em Python, isso acontece quando **não existem mais referências** apontando para o objeto e o garbage collector decide limpar.

Sintaxe:

```python
def __del__(self):
    print("Objeto destruído")
```

Exemplo:

```python
class Conexao:
    def __del__(self):
        print("Encerrando conexão...")
```

Uso:

```python
c = Conexao()
del c  # força a remoção da referência
```

### Observação importante:

* Em Python, destrutores não são muito usados.
* O momento exato em que `__del__` roda não é garantido.
* Para liberar recursos (arquivos, conexões, sockets), preferimos **context managers** (`with`), que são confiáveis.

---

# **Amarrando tudo**

Com isso você já colocou o pé na porta da OO em Python:

1. **OO é um jeito de pensar**: transformar conceitos em objetos.
2. **Classes** definem atributos e comportamentos.
3. **Objetos** são instâncias reais dessas classes.
4. **Construtores** dão vida ao objeto.
5. **Destrutores** limpam recursos (embora raramente usados diretamente).

Esses blocos formam a base da programação orientada a objetos.
