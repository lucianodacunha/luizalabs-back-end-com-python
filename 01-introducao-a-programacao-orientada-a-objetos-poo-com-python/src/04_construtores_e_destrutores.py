class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.tipo = self.__class__.__name__
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __str__(self):
        return f"{self.tipo}: "

    def __del__(self):
        print("Destruindo a classe...")


def main():
    c1 = Cachorro(nome="Rex", cor="Marron")
    print(c1)
    # Chamada explicita do destrutor da classe.
    del c1
    print("finalizando main...")


if __name__ == "__main__":
    main()
    print("finalizando o programa...")
