class Pessoa:
    quantidade = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.quantidade += 1

    @classmethod
    def criar_pessoa(cls, nome, idade):
        # se for preciso ter acesso ao contexto de classe e/ou objeto
        # aqui funciona acessar a classe com cls
        return cls(nome, idade)

    @staticmethod
    def verifica_quantidade():
        # se não for preciso ter acesso ao contexto de classe e/ou objeto
        # aqui não funciona acessar a classe com cls
        return cls.quantidade

    def __str__(self):
        return f"{self.nome}, {self.idade}"


def func1():
    p1 = Pessoa("Pessoa1", 20)
    p2 = Pessoa.criar_pessoa("Pessoa2", 30)
    p3 = Pessoa("Pessoa3", 40)

    print(p1)
    print(p2)
    print(p3)

    print(Pessoa.verifica_quantidade())


if __name__ == "__main__":
    func1()
