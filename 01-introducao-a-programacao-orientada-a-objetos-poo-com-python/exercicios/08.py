class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}"


class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono


def main():
    pessoa = Pessoa("Luciano")
    animal = Animal("Rex", pessoa)

    print(f"{animal.nome} é o animal de {animal.dono}")



if __name__ == "__main__":
    main()
