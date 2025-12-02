# Exercicios 

## **1. Criar uma classe simples `Pessoa`**

Crie uma classe chamada `Pessoa` que tenha dois atributos:

* `nome`
* `idade`

Instancie duas pessoas diferentes e imprima os valores na tela.

---

## **2. Classe com comportamento: `Carro`**

Crie uma classe `Carro` com:

* atributo `velocidade` começando em 0
* métodos `acelerar()` (aumenta +10) e `frear()` (diminui –10, sem ficar negativo)

Instancie um carro e faça-o acelerar e frear algumas vezes.

---

## **3. Criar uma classe com construtor personalizado**

Crie uma classe `Produto` com:

* `nome`
* `preco`
* `quantidade`

O construtor deve receber todos os valores.
Instancie um produto e exiba um resumo:

```
Produto: Nome X | Preço: Y | Quantidade: Z
```

---

## **4. Criar métodos que alteram atributos internos**

Crie uma classe `ContaBancaria` com:

* `titular`
* `saldo` inicial 0

Métodos:

* `depositar(valor)`
* `sacar(valor)` (verificar saldo)

Teste com várias operações.

---

## **5. Criar uma classe com método que retorna valores formatados**

Crie a classe `Aluno` com:

* `nome`
* `notas` (lista)

Método:

* `media()` → retorna a média das notas
* `situacao()` → retorna `"Aprovado"` se média >= 7, senão `"Reprovado"`

Instancie um aluno com notas e verifique situação.

---

## **6. Criar uma classe com *destrutor***

Crie uma classe `ConexaoBD` que:

* imprime `"Conexão iniciada"` no construtor
* imprime `"Conexão encerrada"` no destrutor

Instancie a classe e remova a referência com `del obj`.

(Atenção: o momento exato do destrutor pode variar, mas o exercício é didático.)

---

## **7. Criar uma classe que representa um retângulo**

Classe `Retangulo` com:

* `largura`
* `altura`
* método `area()`
* método `perimetro()`

Instancie um retângulo e imprima área e perímetro.

---

## **8. Criar objetos que interagem entre si**

Crie duas classes:

### `Pessoa`

* `nome`

### `Animal`

* `nome`
* `dono` (um objeto Pessoa)

Exemplo:

```python
p = Pessoa("Luciano")
a = Animal("Rex", p)
```

Imprima:

```
Rex é o animal de Luciano
```

Esse exercício ajuda a entender **composição**.

---

## **9. Criar uma classe com valores padrão e validações**

Crie uma classe `Livro` com:

* `titulo`
* `autor`
* `paginas` (tem que ser > 0)
* construtor com validação (se for <= 0, atribuir 1)

Instancie livros válidos e inválidos.

---

## **10. Criar uma pequena simulação bancária orientada a objetos**

Crie uma classe `Conta` com:

* `numero`
* `titular`
* `saldo` (0 por padrão)

Métodos:

* `depositar(valor)`
* `sacar(valor)`
* `extrato()` → imprime saldo atual

Crie um menu simples para:

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
```

Esse exercício consolida atributos, métodos, construtor e interação entre usuário e objeto.
