from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        # agora os objetos filhos serão obrigados a implementar o método
        ...

    @abstractmethod
    def desligar(self):
        # agora os objetos filhos serão obrigados a implementar o método
        ...

    @property
    @abstractproperty
    def marca(self):
        ...


class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando ...")

    def desligar(self):
        print("desligando...")

    @property
    def marca(self):
        return "Samsung"


def func1():
    cra = ControleRemoto()
    cr = ControleTV()


if __name__ == "__main__":
    func1()
