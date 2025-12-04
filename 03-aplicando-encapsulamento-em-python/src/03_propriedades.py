class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        """ Um setter não deve conter retorno.
        O retorno será realizado pela property
        """
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1


class Pessoa:
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        import datetime
        _ano_atual = int(datetime.datetime.now().strftime("%Y"))
        return _ano_atual - self._nascimento


"""Utilização de encapsulamento com name mangling. Desta forma, o acesso
torna-se ainda mais restrito.
"""
class Carro:
    def __init__(self, marca, cor):
        """ O name mangling altera o nome da variável no objeto.        
        """
        self.__marca = marca
        self.__cor = cor
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade += valor

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

    def __str__(self):
        return f"Velocidade: {self.velocidade}"


def test_carro():
    c = Carro("VW", "Prata'")
    print(c)
    c.acelerar()
    print(c)
    c.frear()
    print(c)
    
def test_foo():
    foo = Foo(10)
    print(foo.x)
    foo.x = 10
    print(foo.x)
    del foo.x
    print(foo.x)


def test_pss():
    pss = Pessoa("Luciano", 1981)
    print(pss.idade)


if __name__ == "__main__":
    test_pss()
