"""
Funções I
"""

# definição de função
def hello():
    print('hello world')


def hello2(saudacao):
    print(saudacao)


def hello3(saudacao="Hello World"):
    print(saudacao)


hello()
hello2("Hello World!")
hello3()
hello3("HELLO WORLD!")

# retorno de funções
def somar(a, b):
    return a + b

print(somar(1, 2))

resultado = somar(2, 3)
print(resultado)

# retornando vários valores
def formatar_string(string):
    return string.lower(), string.upper()

lower, upper = formatar_string("Python")    
print(lower, upper)

# args posicionais e nomeados
def func(a, b):
    return a, b

def func1(a="a", b="b"):
    return a, b

"""
Podemos inverter a ordem, sendo nomeados, o python compreende a posição correta.
"""
print(func("a", "b"))
print(func(b="b", a="a"))

# empacotamento de desempacotamento com args e kwars
"""
Essa palavras chave, são somente uma convenção. Sua utilização, permite ao 
Python, entender os argumentos passados, como tuplas e dicionarios.
Util quando a quantidade de args podem variar.
"""
def func2(*args):
    return sum(args)

print(func2(1, 2, 3, 4, 5))


# O mesmo serve para kwargs, porem com dicionarios.
def func3(**kwargs):
    return kwargs

print(func3(numero=1, string="Python", _float=3.14, boolean=True, funcao=func2))

# escopo

def func4():
    var1 = "Python"

# var1 já nao existe aqui.

var2 = "Python"

def func5():
    # por padrão, var2 não existe aqui. 
    # Para acessa-la, precisamos declara-la como global
    global var2
    print(var2)

func5()

# funcoes como objetos
# podemos passar funções como parametros
def func6(funcao, a, b):
    return funcao(a, b)

print(func6(somar, 1, 2))

# funcoes anonimas
divisao = lambda a, b: a / b

print(divisao(10, 2))
