class Estudante:
    # variaveis de classe
    escola = "Python"
    def __init__(self, nome, matricula):
        # variaveis de instancia
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.escola}"


def _print(*args):
    for i in args:
        print(i)

def func1():
    a = Estudante("E1", 1)
    b = Estudante("E2", 2)    

    _print(a, b)

    # acessando a variavel de classe
    # devemos utilizar a classe
    Estudante.escola = "FastAPI"
    _print(a, b)

    # acessando uma variavel da classe
    Estudante.cidade = "Sao Paulo"
    _print(a, b)

    print(Estudante.__class__.__dict__.items())    


if __name__ == "__main__":
    func1()
