# Decoradores, Iteradores e Geradores

Vamos entrar em um território onde Python revela sua arquitetura mais elegante. Decoradores, iteradores e geradores não são apenas recursos isolados — eles mudam a forma como você pensa e organiza código. São três ferramentas que ampliam o estilo da linguagem de maneiras diferentes: anotando, percorrendo e criando sequências sob demanda.

---

# **Decoradores**

Um decorador é, essencialmente, uma função que recebe outra função e devolve uma versão modificada dela — sem você precisar mexer na função original.

É como colocar um “anel mágico” em uma função, adicionando comportamento extra.
Log de execução, autenticação, medição de tempo, cache — tudo cabe dentro de um decorador.

### **Um exemplo simples**

```python
def logar(funcao):
    def wrapper(*args, **kwargs):
        print(f"Chamando {funcao.__name__}")
        resultado = funcao(*args, **kwargs)
        print(f"{funcao.__name__} terminou")
        return resultado
    return wrapper
```

Usando o decorador:

```python
@logar
def somar(a, b):
    return a + b

somar(2, 3)
```

A sintaxe `@logar` é apenas açúcar sintático para:

```python
somar = logar(somar)
```

### **Quando usar decoradores?**

* Log de chamadas
* Validação de parâmetros
* Controle de acesso (ex.: “usuário logado?”)
* Cache automático de resultados
* Medição de performance
* Funções repetitivas que envolvem “antes e depois”

Decoradores permitem adicionar comportamento transversal sem poluir a função com detalhes.

---

# **Iteradores**

Um iterador é um objeto que sabe ser percorrido passo a passo.
Toda vez que você usa um `for`, existe um iterador trabalhando por trás.

No fundo, um iterador é qualquer objeto que implementa dois métodos:

* `__iter__()` → retorna o próprio iterador
* `__next__()` → retorna o próximo elemento ou levanta `StopIteration`

### **Iterando com o for**

```python
for letra in "Python":
    print(letra)
```

A string não é um iterador, mas é *iterável*.
O Python faz:

```python
iterador = iter("Python")
next(iterador)
next(iterador)
...
```

### **Criando um iterador manualmente**

```python
class Contador:
    def __init__(self, limite):
        self.atual = 0
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual >= self.limite:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor
```

Usando:

```python
for n in Contador(5):
    print(n)
```

Iteradores brilham quando você quer controle fino sobre a forma como os dados são percorridos.

---

# **Geradores**

Geradores são irmãos zen dos iteradores.
Eles seguem a filosofia do “produzir sob demanda”, sem armazenar toda a sequência na memória.

Um gerador é um tipo especial de função que usa `yield` em vez de `return`.
Cada chamada de `yield` pausa a função e devolve um valor — e a função continua exatamente de onde parou no próximo `next()`.

### **Um gerador simples**

```python
def contar(limite):
    n = 0
    while n < limite:
        yield n
        n += 1
```

Uso:

```python
for num in contar(5):
    print(num)
```

Parece um iterador feito à mão, mas a beleza é que o Python constrói todo o protocolo de iteração automaticamente.

### **Geradores são eficientes**

Compare:

```python
lista = [x for x in range(1000000)]   # ocupa memória
gerador = (x for x in range(1000000)) # lazy, quase sem custo
```

Esse `( ... )` cria um *generator expression*, perfeito para pipelines longos ou manipulação de dados sem desperdiçar RAM.

### **Onde geradores brilham?**

* fluxos infinitos
* leitura de arquivos linha a linha
* streams de dados
* pipelines de processamento
* evitar grandes estruturas em memória

Qualquer situação onde “produzir aos poucos” é melhor que “carregar tudo”.

---

# **Amarrando tudo**

Essas três peças formam uma trindade sofisticada do Python:

* **Decoradores** adicionam comportamento sem alterar o núcleo da função.
* **Iteradores** definem como percorrer dados de forma estruturada.
* **Geradores** criam iteradores de maneira natural, eficiente e elegante.

Quando você domina esses três, começa a enxergar Python não como um conjunto de comandos, mas como um ecossistema coerente onde funções, objetos e dados dialogam com fluidez.

---

# **O que é introspecção em Python?**

Em termos simples:

> **Introspecção é a capacidade que um programa tem de examinar seus próprios objetos, tipos, atributos e estrutura enquanto está rodando.**

Python é uma linguagem *altamente introspectiva*.
Quase tudo no sistema é acessível, interrogável e manipulável — você pode inspecionar funções, classes, módulos, objetos, variáveis, parâmetros… tudo.

Isso faz parte do “DNA” filosófico da linguagem: *clareza, transparência e dinamismo*.

---

# **Por que isso importa?**

Introspecção permite:

* descobrir atributos de um objeto sem conhecê-lo previamente
* analisar assinaturas de funções
* depurar com facilidade
* criar ferramentas dinâmicas (como ORMs, frameworks web, decorators, sistemas de plugin)
* escrever código genérico e reutilizável
* melhorar logging, auditoria e debugging

Se você já usou frameworks como FastAPI, Django ou SQLAlchemy, eles estão cheios de introspecção por baixo dos panos.

---

# **Ferramentas introspectivas importantes**

Aqui vão algumas das mais comuns e reveladoras:

### **`type()` – qual é o tipo disso?**

```python
type(10)          # <class 'int'>
type("python")    # <class 'str'>
```

### **`id()` – qual é a identidade (endereço) desse objeto?**

```python
id(objeto)
```

### **`dir()` – que atributos/métodos existem aqui?**

```python
dir("texto")
```

Perfeito para explorar objetos desconhecidos.

### **`help()` – qual é a documentação disso?**

```python
help(list)
```

### **`vars()` – quais atributos internos existem?**

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p = Pessoa("Ana")
vars(p)        # {'nome': 'Ana'}
```

### **`callable()` – isso pode ser chamado?**

```python
callable(len)   # True
callable(10)    # False
```

### **`isinstance()` – esse objeto é instância de quê?**

```python
isinstance(10, int)   # True
```

### **`inspect` – módulo poderoso para introspecção avançada**

```python
import inspect

inspect.getsource(funcao)    # retorna o código da função
inspect.signature(funcao)    # retorna a assinatura
```

---

# **Introspecção e Decoradores**

Decoradores existem, em parte, *porque introspecção existe*.
Eles usam introspecção para acessar:

* o nome da função
* a assinatura
* atributos internos
* docstring
* parâmetros

Exemplo:

```python
def debug(func):
    import inspect
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}{sig}")
        return func(*args, **kwargs)
    return wrapper
```

Sem introspecção, decoradores seriam apenas wrappers cegos.
Com introspecção, eles sabem *quem* estão decorando.

Frameworks como FastAPI usam introspecção para:

* descobrir parâmetros
* identificar tipos
* gerar documentação automática (Swagger)
* validar entrada
* criar rotas dinamicamente

Tudo através do módulo `inspect`.

---

# **Python é introspectivo porque tudo é objeto**

Isso é fundamental.

Em Python:

* funções são objetos
* classes são objetos
* módulos são objetos
* até tipos são objetos (`type` é uma classe)

Ou seja, tudo pode ser inspecionado, modificado, armazenado, passado como argumento.
Essa natureza “tudo é objeto” torna introspecção não uma ferramenta opcional, mas um coração pulsante da linguagem.

---

# **Por que este conceito é valioso para você agora?**

Porque conforme você avança:

* ao trabalhar com **decoradores**, você perceberá que está manipulando funções como objetos introspectáveis
* ao trabalhar com **FastAPI**, vai notar que ele lê assinaturas e tipos dinamicamente
* ao criar **classes mais complexas**, vai querer analisar atributos dinamicamente
* ao criar **ferramentas próprias**, introspecção permite flexibilidade profissional

É um daqueles conceitos que começam pequenos e depois parecem estar em todo lugar.

---
