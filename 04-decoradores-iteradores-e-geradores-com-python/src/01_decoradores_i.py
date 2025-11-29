# passando funções como parâmetro e retornando funções

def obj():
    print("Hello")


def func(param):
    return param


func(obj)()


# funções aninhadas

def externa(param):

    print("Função externa")

    def interna1():
        print("Função interna1")

    def interna2():
        print("Função interna2")

    if param == 1:
        interna1()
    elif param == 2:
        interna2()
    else:
        return


externa(1)


# decoradores
def imprimir1():
    print("Hello1")

def decorador1(func):
    def envelope1():
        print("Executando meu primeiro decorador1...")
        func()
        print("Decorador1 finalizado!")
    return envelope1


imprimir1 = decorador1(imprimir1)
imprimir1()


def decorador2(func):
    def envelope2():
        print("Executando meu segundo decorador2...")
        func()
        print("Decorador2 finalizado!")
    return envelope2

@decorador2
def imprimir2():
    print("Hello2")

# imprimir2 = decorador2(imprimir2)
imprimir2()


# decorador com args/kwargs
def decorador3(func):
    def envelope3(*args, **kwargs):
        print("Executando meu terceiro decorador3...")
        func(*args, **kwargs)
        print("Decorador3 finalizado!")
    return envelope3

@decorador3
def imprimir3(param):
    print(f"{param}")

# imprimir3 = decorador3(imprimir3)
imprimir3("Hello3")


# retornando valor da função principal
# decorador com args/kwargs
def decorador4(func):
    def envelope4(*args, **kwargs):
        print("Executando meu quarto decorador4...")
        result = func(*args, **kwargs)
        print("Decorador4 finalizado!")
        return result
    return envelope4

@decorador4
def imprimir4(param):
    return f"{param}"

print(imprimir4("Hello4"))

# introspecção, capacidade de examinar seus próprios objetos.
print(print.__name__)

# porém, quando tentamos fazer isso com nossa função imprimir
print(imprimir4.__name__)

# podemos utilizar functools para resolver
import functools

def decorador5(func):
    @functools.wraps(func)
    def envelope5(*args, **kwargs):
        print("Executando meu quarto decorador5...")
        result = func(*args, **kwargs)
        print("Decorador5 finalizado!")
        return result
    return envelope5

@decorador5
def imprimir5(param):
    return f"{param}"

print(imprimir5.__name__)
