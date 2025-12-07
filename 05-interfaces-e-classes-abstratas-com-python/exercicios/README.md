Claro — aqui estão **10 exercícios bem estruturados** para praticar exatamente os tópicos:
**variáveis de classe x instância, métodos de classe, métodos estáticos, interfaces (jeito Pythonico), classes abstratas e até mixins**.
Eles crescem em dificuldade e te colocam para aplicar cada conceito de forma concreta.

---

# **1. Variável de classe vs variável de instância**

Crie uma classe `Pessoa` com:

* variável de classe `especie = "Humano"`
* atributos de instância: `nome`, `idade`

Instancie várias pessoas e verifique:

1. Que todas veem a mesma variável de classe.
2. Que mudar `p1.especie` cria um atributo de instância, não muda a classe.

---

# **2. Contador de instâncias**

Crie uma classe `Carro` com:

* variável de classe `total = 0`
* construtor que incrementa `total` a cada novo carro

Instancie três carros e exiba `Carro.total`.

Esse exercício treina a diferença entre classe e instância.

---

# **3. Método de classe como *factory***

Crie uma classe `Usuario` com:

* `nome`
* `email`

Crie um método de classe:

```python
@classmethod
def com_email_padrao(cls, nome)
```

Esse método deve criar o usuário com email `"nome@empresa.com"`.
Instancie usuários com e sem factory e compare.

---

# **4. Método estático utilitário**

Crie uma classe `MathHelper` contendo:

```python
@staticmethod
def eh_par(n)
```

que retorna True/False.

A classe não deve precisar de instâncias.
Use o método em uma lista de números para filtrar os pares.

---

# **5. Interface por duck typing**

Crie três classes:

* `Carro` com método `mover()`
* `Bicicleta` com método `mover()`
* `Pessoa` com método `mover()`

Crie uma função:

```python
def iniciar_movimento(obj):
    obj.mover()
```

Passe objetos de tipos diferentes.
Nenhuma classe deve herdar de ninguém — apenas implemente o método.

---

# **6. Interface formal usando ABC**

Use:

```python
from abc import ABC, abstractmethod
```

Crie classe abstrata `Pagamento` com método abstrato `pagar(valor)`.

Subclasses:

* `Pix`
* `CartaoCredito`
* `Boleto`

Cada uma implementa `pagar`.
Crie uma lista de pagamentos e chame `pagar` sem verificar o tipo.

Treina polimorfismo via contrato.

---

# **7. Método abstrato + implementação parcial**

Crie classe abstrata `Animal` com método abstrato `falar()`
e um método concreto:

```python
def dormir(self):
    print("zzz…")
```

Subclasses:

* `Cachorro`
* `Gato`

Implemente `falar()` em cada uma.
Teste chamando `falar()` e `dormir()`.

---

# **8. Mixins**

Crie um mixin `LogMixin` com método:

```python
def log(self, msg):
    print(f"[LOG] {msg}")
```

Agora crie uma classe `Servico` que herda do mixin e adiciona:

```python
def executar(self):
    self.log("Executando serviço...")
```

Instancie `Servico` e teste.
Treina composição via herança múltipla.

---

# **9. Classe abstrata + método de classe fábrica**

Crie a classe abstrata `Shape` com método abstrato `area()`.

Crie subclasses:

* `Quadrado`
* `Circulo`

Na classe base, crie um `@classmethod` chamado `from_string` que recebe uma string como:

```
"quadrado:5"
"circulo:3"
```

E retorna a instância correspondente.

Ex.: `Shape.from_string("quadrado:5")`.

Esse exercício combina **classe abstrata, factory method e polimorfismo**.

---

# **10. Sistema completo integrando vários conceitos**

Crie:

* Classe abstrata `Mensagem` com método `enviar()`.
* Subclasses: `Email`, `SMS`, `Push`.
* Um mixin `LogMixin` para registrar atividade.
* Faça as subclasses herdarem tanto de `Mensagem` quanto de `LogMixin`.
* Variável de classe `total_enviadas`.
* Método estático `validar_texto(msg)`.

Ao enviar uma mensagem:

* validar o texto com método estático
* registrar no log via mixin
* incrementar o contador de classe

Depois crie uma lista com vários tipos de mensagens e processe todas via polimorfismo.

Esse exercício junta tudo:
**herança, polimorfismo, métodos de classe/estáticos, mixins, variáveis de classe, classes abstratas**.

