# Trabalhando com Listas em Python

Listas são uma das estruturas mais versáteis e “vivas” do Python. Elas funcionam como pequenas prateleiras dinâmicas: você pode colocar itens, tirar, reorganizar, misturar tipos diferentes e até aninhar listas dentro de listas. 

---

## **Uma breve introdução**

Uma lista em Python é:

* ordenada
* mutável
* heterogênea (aceita qualquer tipo dentro dela)

Pense nela como uma sequência onde cada elemento tem uma posição (índice) e você pode alterar o conteúdo sempre que quiser.

```python
frutas = ["maçã", "pera", "uva"]
```

A ordem importa: `"maçã"` está no índice 0, `"pera"` no 1, `"uva"` no 2.

O fato de ser mutável significa que a lista pode crescer, encolher, trocar elementos e mudar de forma ao longo do tempo — muito útil em algoritmos, coleções dinâmicas e manipulação de dados.

---

## **Criação e acesso aos dados**

### **Criando listas**

A forma mais comum é usando `[]`:

```python
numeros = [1, 2, 3, 4, 5]
mistura = [1, "texto", 3.14, True]
```

Também dá para criar listas vazias:

```python
vazia = []
vazia = list()
```

E listas aninhadas (listas dentro de listas):

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
```

### **Acessando elementos**

O acesso é feito com colchetes e índice:

```python
frutas = ["maçã", "pera", "uva"]
frutas[0]   # "maçã"
frutas[1]   # "pera"
```

Índices negativos contam de trás para frente:

```python
frutas[-1]  # "uva"
frutas[-2]  # "pera"
```

### **Modificando elementos**

Por serem mutáveis, listas aceitam:

```python
frutas[1] = "abacate"
```

Agora a lista vira:

```python
["maçã", "abacate", "uva"]
```

### **Fatiamento em listas**

Funciona como em strings:

```python
numeros = [10, 20, 30, 40, 50]

numeros[1:3]   # [20, 30]
numeros[:2]    # [10, 20]
numeros[::2]   # [10, 30, 50]
```

---

## **Métodos úteis da classe `list`**

As listas têm um conjunto de métodos que tornam o trabalho com coleções extremamente flexível.

### **Adicionar elementos**

```python
append(x)     # adiciona no final
extend([...]) # adiciona vários valores
insert(i, x)  # insere na posição i
```

Exemplos:

```python
frutas.append("kiwi")
frutas.extend(["banana", "mamão"])
frutas.insert(1, "laranja")
```

### **Remover elementos**

```python
remove(x)     # remove a primeira ocorrência de x
pop(i)        # remove o item da posição i (ou o último se não passar i)
clear()       # remove tudo
```

Exemplos:

```python
frutas.remove("kiwi")
frutas.pop(0)        # remove o primeiro elemento
frutas.clear()       # lista fica vazia
```

### **Busca e contagem**

```python
count(x)     # quantas vezes x aparece
index(x)     # primeira posição em que x aparece
```

Exemplos:

```python
numeros = [1, 2, 2, 3]
numeros.count(2)   # 2
numeros.index(3)   # 3
```

### **Ordenação**

```python
sort()        # ordena a própria lista
sorted(lista) # cria nova lista ordenada
```

Exemplos:

```python
nums = [3, 1, 4, 2]
nums.sort()            # [1, 2, 3, 4]
sorted(nums)           # cria nova lista ordenada
```

Você pode ordenar com `key=` e `reverse=`:

```python
nomes.sort(key=len)       # ordena pelo tamanho
nomes.sort(reverse=True)  # ordem invertida
```

### **Outros métodos úteis**

```python
copy()      # cópia rasa
reverse()   # inverte a lista (sem criar nova)
```

Exemplos:

```python
lista = [1, 2, 3]
lista.reverse()       # [3, 2, 1]
```

---

## **Listas como base para raciocínio Python**

Quando você domina listas, metade da linguagem se abre. Loops se tornam naturais, compreensões de lista viram ferramentas elegantes, e manipulação de dados fica muito mais fluida.

Quer transformar cada número de uma lista?

```python
quadrados = [x**2 for x in range(6)]
```

Quer filtrar?

```python
pares = [x for x in range(10) if x % 2 == 0]
```

Esse estilo elegante nasce da força e flexibilidade que as listas oferecem.
