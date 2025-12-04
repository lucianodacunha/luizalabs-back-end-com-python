# Exercícios

## **1. Atributo privado com acesso controlado**

Crie uma classe `Pessoa` com:

* atributo privado `__cpf`
* método público `mostrar_cpf()`

Instancie a classe e demonstre que:

* acessar diretamente `p.__cpf` gera erro
* acessar via método funciona

---

## **2. Criar getters e setters com validação**

Crie uma classe `Produto` com:

* atributo protegido `_preco`
* propriedade `preco` com setter que:

  * não permite valores negativos

Teste atribuindo valores válidos e inválidos.

---

## **3. Propriedade somente leitura**

Crie uma classe `Carro` com:

* atributos `_marca` e `_modelo`
* propriedade somente leitura `descricao` que retorna `"Marca Modelo"`

Instancie e tente alterar `carro.descricao` para provocar erro.

---

## **4. Controle de saldo com encapsulamento**

Crie uma classe `Conta` com:

* atributo privado `__saldo`
* método `depositar(valor)`
* método `sacar(valor)` com validação
* propriedade `saldo` apenas para leitura

Garanta que não seja possível definir `conta.saldo = 100`.

---

## **5. Encapsulamento + regras internas**

Crie classe `Aluno` com:

* atributo `_notas`, uma lista
* método `adicionar_nota(n)` (0 a 10)
* propriedade calculada `media`
* propriedade `situacao` (aprovado se média ≥ 7)

Teste cenários diferentes.

---

## **6. Atributos privados + property calculada**

Crie a classe `Triangulo` com atributos privados:

* `__base`
* `__altura`

Propriedades:

* `base` e `altura` (com setter)
* `area` (somente leitura, calculada)

Teste alterando base e altura dinamicamente.

---

## **7. Encapsular temperatura com conversão automática**

Crie classe `Temperatura` com atributo privado `__celsius`.

Propriedades:

* `celsius` (get/set)
* `fahrenheit` (get: converte automaticamente, set: converte e atualiza celsius)

Exemplo:

```python
t = Temperatura(0)
print(t.fahrenheit)   # 32
t.fahrenheit = 212
print(t.celsius)      # 100
```

---

## **8. Proteger mudanças internas com métodos controlados**

Crie classe `Pedido` com:

* atributo privado `__status`
* método `avancar_status()` que segue a cadeia:
  `"novo" → "processando" → "enviado" → "concluído"`
* propriedade `status` somente leitura

Tentar fazer `pedido.status = "cancelado"` deve falhar.

---

## **9. Bloquear criação de atributos arbitrários**

Crie classe `Cliente` usando:

```python
__slots__ = ("nome", "_idade")
```

E crie uma propriedade `idade` com validação (> 0).

Teste tentar criar `cliente.endereco = "x"` e veja o erro.

---

## **10. Mini-sistema orientado a encapsulamento**

Crie classe `Funcionario` com:

* atributo privado `__salario`
* propriedade `salario`:

  * leitura: retorna o valor
  * escrita: só permite aumento, nunca redução

Crie classe `Gerente(Funcionario)` que:

* permite aplicar bônus via método `aplicar_bonus(percentual)`
* não permite acessar nem modificar diretamente o salário base

Instancie, mexa nos valores e comprove que:

* o salário está protegido
* só aumenta via regras da classe
* a hierarquia respeita o encapsulamento
