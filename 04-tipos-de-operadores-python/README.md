# Tipos de operadores em Python

Python trata operadores como um pequeno arsenal semântico: cada símbolo expressa uma relação entre valores, e entender isso bem deixa o código mais fluido e — curiosamente — mais expressivo. Vamos passear por cada categoria com calma, com exemplos simples e um pouco de contexto para você encaixar mentalmente.

Nada disso precisa ser decorado; a graça está em ver o padrão se revelar.

---

## **Operadores aritméticos**

Eles fazem as contas do dia a dia. Python trata números como cidadãos de primeira classe, então quase tudo funciona como você espera.

```python
a + b     # soma
a - b     # subtração
a * b     # multiplicação
a / b     # divisão (sempre float)
a // b    # divisão inteira (descarta a parte decimal)
a % b     # módulo (resto da divisão)
a ** b    # exponenciação
```

Exemplo suave:

```python
3 ** 2      # 9
10 // 3     # 3
10 % 3      # 1
```

Python evita surpresas: `10 / 2` sempre vira `5.0`, não `5`.

---

## **Operadores de comparação**

Eles respondem perguntas — literalmente. Sempre retornam `True` ou `False`.

```python
a == b     # igual
a != b     # diferente
a > b      # maior
a < b      # menor
a >= b     # maior ou igual
a <= b     # menor ou igual
```

Exemplo:

```python
"python" == "Python"   # False (case sensitive)
5 >= 3                  # True
```

Comparação é a base de qualquer lógica.

---

## **Operadores lógicos**

São os conectores do pensamento: ajudam Python a raciocinar com proposições.

```python
and       # os dois precisam ser verdadeiros
or        # basta um ser verdadeiro
not       # inverte a condição
```

Exemplo:

```python
idade = 25
tem_carteira = True

idade >= 18 and tem_carteira   # True
```

Python avalia expressões da esquerda para a direita e faz *short-circuit*: se já sabe o resultado, nem olha o resto.

---

## **Operadores de identidade**

Agora entramos no território mais sutil. Identidade não verifica “valor igual”; ela verifica se duas variáveis apontam para **o mesmo objeto na memória**.

```python
is
is not
```

Exemplo:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b      # True  (mesmo objeto)
a is c      # False (valores iguais, objetos diferentes)
a == c      # True
```

Muita gente confunde `is` com `==`.
Regra de bolso: **use `is` apenas com `None`**, por exemplo:

```python
if valor is None:
    ...
```

---

## **Operadores de associação (membership)**

Eles respondem “isso pertence a isso?”.

```python
in
not in
```

Funcionam com strings, listas, dicionários, sets…

Exemplo:

```python
"py" in "python"          # True
3 in [1, 2, 3]            # True
"idade" in {"idade": 20}  # True (checa chaves)
```

Associação é o jeito Python de fazer buscas rápidas e naturais.

---

## **Operadores de atribuição**

Atribuição é onde valores “ganham um nome”. E Python permite versões compactas para atualizar valores.

```python
x = 10     # atribuição simples
x += 1     # x = x + 1
x -= 2     # x = x - 2
x *= 3     # x = x * 3
x /= 2     # x = x / 2
x %= 2     # resto
x //= 3    # divisão inteira
x **= 2    # potenciação
```

Eles têm um charme especial porque permitem código expressivo e direto, sem redundância.

Exemplo:

```python
contador = 0
contador += 1
```

---

## **Um detalhe interessante: operadores também são funções por baixo**

Por exemplo:

```python
3 + 4
```

por baixo dos panos é:

```python
operator.add(3, 4)
```

Isso explica por que Python permite sobrecarga de operadores em classes próprias (coisa que vira um parque de diversão em estruturas matemáticas, geometrias, etc.).

---

## Amarrando tudo

Quando você junta:

• aritméticos (quantos?)
• comparação (é igual?)
• lógicos (e/ou/não)
• identidade (é o mesmo objeto?)
• associação (está dentro?)
• atribuição (guarde isso com este nome)

… você tem o núcleo do raciocínio computacional no Python.
É como se cada operação fosse um verbo na linguagem, e compor frases lógicas vira quase natural.
