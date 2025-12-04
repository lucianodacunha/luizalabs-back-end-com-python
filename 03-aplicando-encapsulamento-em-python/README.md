# Aplicando Encapsulamento em Python

## **O que é Encapsulamento?**

Encapsulamento é o princípio que diz:

> “Os dados internos de um objeto devem ser protegidos e acessados apenas da maneira correta.”

É como separar o “motor interno” da “interface externa”.
Você oferece métodos públicos para usar o objeto, enquanto mantém a lógica interna organizada, segura e separada.

Por que isso é útil?

* evita manipulação indevida
* protege estados internos
* permite controle e validação
* melhora manutenção do código
* cria APIs mais limpas e previsíveis

Encapsular é, essencialmente, proteger a integridade do objeto.

---

## **Recursos Públicos e Privados em Python**

Diferente de linguagens como Java ou C++, Python **não tem modificadores de acesso rígidos** (como `private`, `protected`, `public`).
Mas tem uma convenção (e alguns truques) muito eficientes.

#### **1. Atributos públicos**

Acessíveis normalmente:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # público
```

Uso:

```python
p = Pessoa("Ana")
print(p.nome)
```

Python não impede o acesso externo — você é livre, mas espera-se sabedoria.

---

#### **2. Atributos “protegidos” (convenção)**

Prefixo com **um único underscore**:

```python
self._saldo = 0
```

Essa é a forma Python de dizer:

> “Isso é interno. Você *pode* acessar, mas estamos fazendo um acordo de cavalheiros de que não deve.”

É uma proteção **organizacional**, não técnica.

---

#### **3. Atributos privados (com name-mangling)**

Prefixo com **dois underlines**:

```python
self.__senha = "1234"
```

Aqui sim existe uma proteção técnica leve: o Python aplica *name mangling* e renomeia internamente o atributo para algo como:

```
_Pessoa__senha
```

Tentativas diretas falham:

```python
p.__senha  # erro
```

Mas ainda é acessível via o nome alterado:

```python
p._Pessoa__senha
```

O objetivo não é trancar o atributo como um cofre inseguro, mas dificultar acessos acidentais.

---

## **Propriedades: a joia do encapsulamento em Python**

Propriedades (`@property`) são uma das ferramentas mais elegantes e poderosas do encapsulamento em Python.

Imagine que você tem um atributo “simples”:

```python
p.idade = 30
```

E amanhã decide que idade precisa ser validada, calculada ou registrada num log. Em outras linguagens, isso demandaria mudar o código em todos os lugares que acessam `idade`.

Em Python:

1. Primeiro você começa com um atributo simples:

```python
class Pessoa:
    def __init__(self, idade):
        self.idade = idade
```

2. Depois pode transformá-lo em uma propriedade sem mudar o uso externo:

```python
class Pessoa:
    def __init__(self, idade):
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade = valor
```

E no código do usuário:

```python
p = Pessoa(20)
p.idade = 30       # setter
print(p.idade)     # getter
```

Parece um atributo?
Sim.
Mas por trás há lógica, validação, proteção.

Isso é encapsulamento em sua forma mais natural.

---

## **Getter e Setter: como funcionam no Python moderno**

Getter → método que retorna um valor.

Setter → método que altera o valor.

Mas Python não usa a sintaxe:

```python
p.getIdade()
p.setIdade(30)
```

Isso fica para linguagens tradicionais.
Python prefere **propriedades**, porque deixam o código mais limpo.

O mecanismo:

```python
@property
def saldo(self):
    return self._saldo

@saldo.setter
def saldo(self, valor):
    if valor < 0:
        raise ValueError("Saldo negativo não permitido.")
    self._saldo = valor
```

O uso externo continua parecendo “atributos simples”, mas por dentro é comportamento.

---

## **Encapsulamento e comportamento seguro**

Encapsular é criar limites claros:

### Sem encapsulamento

```python
conta.saldo -= 999999   # opa 😬
```

### Com encapsulamento

```python
conta.sacar(999999)  # o método pode proteger regras internas
```

Encapsulamento não é só “bloquear atributos”, mas **exigir que o objeto seja usado do jeito certo**.

---

## **Propriedades somente leitura**

Algo muito comum:

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco
```

Não tem setter → atributo **somente leitura**.

---

## **Propriedades calculadas (muito úteis)**

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura
```

Uso:

```python
r = Retangulo(10, 5)
print(r.area)  # 50
```

Repara: `area` parece atributo, mas é método calculado.

Isso cria APIs extremamente naturais.

---

## **Encapsulamento e coerência interna**

Encapsular não é esconder:
é garantir consistência.

Exemplo clássico:

```python
class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo
```

O objeto controla seu estado.
É o próprio objeto que decide:

* como muda
* quando muda
* por qual regra

Encapsulamento é autonomia.

---

## **Extra (útil): slots para otimização**

O Python permite restringir atributos possíveis usando:

```python
__slots__ = ("saldo", "titular")
```

Isso:

* economiza memória
* impede criação de atributos arbitrários (erro se tentar)

Embora não seja propriamente encapsulamento, ajuda a controlar a **estrutura interna**.

---

## **Amarrando o conceito**

Encapsulamento em Python funciona assim:

1. **Atributos públicos:** livre acesso.
2. **Atributos protegidos (`_atributo`):** convenção interna.
3. **Atributos privados (`__atributo`):** name mangling para proteção extra.
4. **Propriedades (`@property`):** getter/setter com sintaxe elegante.
5. **Métodos específicos para controlar comportamento:** o objeto gerencia sua lógica.
6. **Uso responsável:** Python confia mais no programador do que na linguagem para impor limites.

Encapsular é sobre clareza de intenção, segurança conceitual e API expressiva.

---

Se quiser, posso:

* criar **10 exercícios** sobre encapsulamento
* comparar encapsulamento em Python com Java/C++
* construir uma **classe bancária completa** aplicando propriedades e validações
* mostrar encapsulamento usando **dataclasses** com `@property` integrados

É só escolher o próximo degrau.
