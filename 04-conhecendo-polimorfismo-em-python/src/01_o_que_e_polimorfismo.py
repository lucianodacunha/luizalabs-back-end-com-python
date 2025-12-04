# como exemplo mais básico, temos a função builtin len.

def func0():
    print(len("python"))
    print(len([1, 2, 3, 4]))

# pois recebe dois tipos de dados e consegue tratar. Isso é típico de um
# comportamento polimórfico.

# basicamente, essa função funciona mais ou menos assim:
class Pai:
    def __init__(self, valor):
        self.valor = valor

    def test(self):
        print(self.valor)


class Filho1(Pai):
    def __init__(self, valor):
        super().__init__(valor)


class Filho2(Pai):
    def test(self):
        print(len(self.valor))


class ProcessaFamilia:
    def imprimir(self, x):
        print(f"Tipo: {x.__class__.__name__}: ", end="")
        print({x.test()})
        print()
        


def func1():
    p = Pai("a")
    p.test()

    f1 = Filho1("a1")
    f1.test()

    f2 = Filho2("a")
    f2.test()    

def func2():
    p = Pai("a")
    f1 = Filho1("a1")
    f2 = Filho2("a")

    pf = ProcessaFamilia()
    for i in [p, f1, f2]:
        pf.imprimir(i)


# porém, não depende exclusivamente de herança
class A:
    def x(self): 
        print("Mensagem 1")


class B:
    def x(self): 
        print("Mensagem 2")


class C:
    def x(self): 
        print("Mensagem 3")


class D:
    def p(self, _cls):
        _cls.x()


def func3():

    a = A()
    b = B()
    c = C()
    d = D()

    for i in [a, b, c]:
        d.p(i)


# Outra forma de utilizar polimorfismo, é implementar com classes abstratas.
# Com classes abstratas, é possível obrigar classes filhas a implementar métodos
# desejados.
# Sem classes abstratas, essa obritoriedade não existe, deixando a carga do 
# programador.


if __name__ == "__main__":
    func3()
