# Exercícios

## **1. Herança simples: Animal → Cachorro**

Crie a classe base `Animal` com:

* atributo: `nome`
* método: `emitir_som()` (imprima “Som genérico”)

Crie a subclasse `Cachorro` que:

* sobrescreve `emitir_som()` para imprimir “Au au!”

Instancie ambos e teste.

---

## **2. Reaproveitando construtor da classe pai**

Crie a classe `Pessoa` com:

* `nome`
* `idade`

Agora crie `Estudante(Pessoa)` com:

* atributo extra: `matricula`

Use `super()` no construtor.

---

## **3. Sobrescrita de métodos**

Classe `Conta` com:

* `saldo`
* método `sacar(valor)` que verifica se há saldo

Classe `ContaEspecial(Conta)` com:

* atributo `limite`
* sobrescreva `sacar(valor)` para considerar o limite

Teste os dois comportamentos.

---

## **4. Polimorfismo simples**

Crie três subclasses de `Forma`:

* `Quadrado`
* `Retangulo`
* `Circulo`

Todas devem implementar o método `area()`.
Crie uma lista com várias formas e calcule a área de todas usando um loop, explorando polimorfismo.

---

## **5. Herança múltipla controlada**

Classe `Volador`:

* método `voar()` → imprime “Voando…”

Classe `Nadador`:

* método `nadar()` → imprime “Nadando…”

Classe `Pato(Volador, Nadador)`
Teste se o pato herda ambos comportamentos.

---

## **6. Usando MRO para entender prioridades**

Crie:

```python
class A:
    def fazer(self): print("A")

class B(A):
    def fazer(self): print("B")

class C(A):
    def fazer(self): print("C")

class D(B, C):
    pass
```

Instancie `D` e chame `fazer()`.
Depois imprima o MRO:

```python
print(D.mro())
```

Explique a ordem de resolução.

---

## **7. Extensão da classe pai (adicionando atributos)**

Crie `Funcionario(Pessoa)` com:

* salário
* método `aumento(percentual)`

O método deve aumentar apenas o salário, mantendo nome e idade como estão.

---

## **8. Classe abstrata com método obrigatório**

Crie:

```python
from abc import ABC, abstractmethod
```

Classe base `Veiculo(ABC)` com método abstrato `mover()`.

Subclasses:

* `Carro`
* `Bicicleta`

Ambas devem implementar `mover()` de forma diferente.
Tente instanciar `Veiculo` e veja o erro.

---

## **9. Exercício de substituição Liskov (LSP)**

Crie:

* `Funcionario` com método `calc_salario()`
* `Gerente` que recebe bônus extra e sobrescreve `calc_salario()`

Crie uma função:

```python
def imprimir_salario(funcionario):
    print(funcionario.calc_salario())
```

Mostre que a função aceita ambos (polimorfismo).

---

## **10. Mini-sistema de biblioteca**

Crie:

* Classe base `ItemBiblioteca` com:

  * `titulo`
  * método `informacoes()`

* Subclasses:

  * `Livro` (tem autor)
  * `Revista` (tem edição)
  * `DVD` (tem duração)

Sobrescreva `informacoes()` em cada subclasse para mostrar detalhes específicos.

Crie uma lista mista com livros, revistas e DVDs e percorra chamando `informacoes()`.
