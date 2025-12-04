# Exercícios

## **1. Polimorfismo básico: Animal → subclasses**

Crie a classe base `Animal` com método `falar()`.
Crie três subclasses:

* `Cachorro` → “Au au!”
* `Gato` → “Miau!”
* `Vaca` → “Muuu!”

Coloque objetos em uma lista e faça todos falarem usando um único loop.

---

## **2. Polimorfismo com método sobrescrito**

Crie a classe `Forma` com método `area()`.
Crie subclasses:

* `Quadrado(lado)`
* `Retangulo(largura, altura)`
* `Circulo(raio)`

Use polimorfismo para calcular áreas sem perguntar o tipo da forma.

---

## **3. Função genérica que aceita qualquer “tocador de som”**

Sem herança desta vez!

Crie classes:

* `Radio` com método `tocar()`
* `Violao` com método `tocar()`
* `Piano` com método `tocar()`

Agora crie uma função:

```python
def executar(obj):
    obj.tocar()
```

E passe objetos de tipos diferentes para ela.
Esse exercício treina *duck typing*.

---

## **4. Polimorfismo + herança + sobrescrita parcial**

Classe base `Funcionario` com método `calcular_pagamento()`.
Subclasses:

* `FuncionarioHorista`
* `FuncionarioMensalista`
* `Estagiario`

A função deve funcionar para qualquer um.

---

## **5. Polimorfismo com classes abstratas (ABC)**

Use:

```python
from abc import ABC, abstractmethod
```

Crie uma classe abstrata `Veiculo` com método abstrato `mover()`.
Subclasses:

* `Carro`
* `Navio`
* `Aviao`

Todos devem implementar `mover()`.
Crie uma lista de veículos e processe todos em um loop.

---

## **6. Sobrescrita de construtor + polimorfismo**

Crie a classe base `Mensagem` com atributo `texto` e método `enviar()`.
Subclasses:

* `Email`
* `SMS`
* `NotificacaoPush`

Cada uma imprime uma mensagem diferente na tela ao enviar.

Instancie todas e use a mesma função para processá-las:

```python
def enviar_mensagem(msg):
    msg.enviar()
```

---

## **7. Sistema de pagamentos polimórfico**

Classe base `Pagamento` com método `pagar(valor)`.
Subclasses:

* `Pix`
* `CartaoCredito`
* `Boleto`

Crie uma função que receba qualquer objeto de pagamento e execute `pagar(valor)`
sem diferença no código.

---

## **8. Polimorfismo em coleções heterogêneas**

Crie classes:

* `Video` com método `reproduzir()`
* `Musica` com método `reproduzir()`
* `Podcast` com método `reproduzir()`

Agora crie uma playlist com mistura de objetos dessas classes e faça todos serem reproduzidos numa única função usando polimorfismo.

---

## **9. Polimorfismo com exceções e fallback**

Crie classes:

* `Imagem` com método `renderizar()`
* `Audio` com método `play()`
* `Video` com ambos (`renderizar` e `play`)

Agora crie uma função:

```python
def executar(obj):
    tente rodar .play()
    se não existir, tente rodar .renderizar()
    se não existir, imprima "Objeto não executável"
```

Treina polimorfismo através de tentativa de interface.

---

## **10. Polimorfismo aplicado a relatórios**

Crie classe base `Relatorio` com método `gerar()`.
Crie subclasses:

* `RelatorioPDF`
* `RelatorioCSV`
* `RelatorioHTML`

Cada uma imprime uma mensagem diferente simulando geração do arquivo.

Agora crie uma função:

```python
def gerar_relatorio(relatorio):
    relatorio.gerar()
```

E teste com múltiplos tipos de relatório, demonstrando como o código permanece o mesmo.
