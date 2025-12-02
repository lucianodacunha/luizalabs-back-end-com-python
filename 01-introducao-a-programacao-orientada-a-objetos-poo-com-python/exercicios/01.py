class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


def main():
    p1 = Pessoa("Luciano", 40)
    p2 = Pessoa("Luciana", 50)

    print(f"Pessoa 1: {p1.nome}, {p1.idade}")
    print(f"Pessoa 2: {p2.nome}, {p2.idade}")


if __name__ == "__main__":
    main()
