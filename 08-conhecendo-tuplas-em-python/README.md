# Conhecendo Tuplas em Python

Tuplas são como listas que fizeram voto de silêncio: elas guardam dados, mas não permitem mudanças depois de criadas. Essa imutabilidade dá a elas um charme próprio e usos muito específicos — desde segurança lógica até velocidade e uso como chaves em dicionários.

---

## **Uma breve introdução**

Uma tupla é:

* ordenada
* indexada
* imutável
* capaz de armazenar tipos mistos

O mais importante aqui é a **imutabilidade**: depois que você cria uma tupla, seus elementos não podem ser alterados, adicionados ou removidos.
Ela vira um “registro congelado”.

Criação básica:

```python
coordenada = (21.8271, -47.2492)
```

Tuplas são ótimas para representar dados que não devem mudar: coordenadas, dias da semana, configurações fixas, etc.

---

## **Criação e acesso aos dados**

### **Criando tuplas**

A forma mais comum é com parênteses:

```python
pessoa = ("Ana", 30, "SP")
```

Uma tupla com um único item precisa de vírgula:

```python
um_elemento = (42,)   # tupla
nao_e_tupla = (42)    # inteiro normal
```

Você também pode criar tuplas sem parênteses — o Python entende:

```python
t = 1, 2, 3
```

Isso se chama *tuple packing*.

### **Acessando elementos**

Funciona exatamente como listas:

```python
dias = ("seg", "ter", "qua")

dias[0]      # "seg"
dias[-1]     # "qua"
```

### **Fatiando tuplas**

Também idêntico às listas:

```python
dias[:2]     # ("seg", "ter")
dias[::-1]   # ("qua", "ter", "seg")
```

### **Desempacotamento elegante**

Tuplas brilham forte aqui:

```python
x, y = (10, 20)
```

Ou ainda:

```python
a, b, c = 1, 2, 3
```

E até:

```python
a, *meio, b = (1, 2, 3, 4, 5)
```

Esse “*desempacotamento inteligente*” é uma das razões pelas quais tuplas são tão usadas.

---

## **Métodos da classe `tuple`**

Por serem imutáveis, as tuplas têm pouquíssimos métodos — só dois:

### **count(x)**

Conta quantas vezes um valor aparece:

```python
t = (1, 2, 2, 3)
t.count(2)    # 2
```

### **index(x)**

Retorna a primeira posição de um valor:

```python
t.index(3)    # 3
```

E só.
Nada de `append`, `remove`, `sort` — tuplas não mudam.

Mas essa “rigidez” é justamente o ponto: quando você quer garantir que ninguém altere os dados sem querer, a tupla é a guardiã.

---

## **Quando usar tupla em vez de lista?**

Uma boa regra mental:

* **Use lista** quando os dados mudam — coleções dinâmicas.
* **Use tupla** quando os dados são fixos — registros imutáveis.

Exemplos clássicos para tuplas:

• coordenadas (lat, lon)
• configurações constantes
• resultados múltiplos retornados por funções
• chaves de dicionários compostas
• ordem de colunas fixa em DataFrames manuais

Tupla transmite a intenção de estabilidade.

---

## **O detalhe elegante: retorno de múltiplos valores**

Funções retornam uma tupla automaticamente:

```python
def stats(lista):
    return min(lista), max(lista)

menor, maior = stats([3, 8, 1])
```

Python deixa isso tão natural que nem parece tupla — mas é.

---

## **Amarrando tudo**

Tuplas são listas que decidiram viver uma vida contemplativa: não mudam, não se movem, só representam.
Essa estabilidade as torna valiosas em vários contextos do Python, especialmente quando você quer clareza sem risco de mutação acidental.
