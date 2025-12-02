class Carro:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        print("acelerando...")
        self.velocidade += 10

    def frear(self):
        if self.velocidade - 10 >= 0:
            print("desacelerando...")
            self.velocidade -= 10
        elif self.velocidade == 0:
            print("já esta parado!")
        else:
            print("parando...")
            self.velocidade = 0

    def __str__(self):
        return f"Velocidade atual: {self.velocidade}"


def main():
    carro = Carro()
    print(carro)
    carro.acelerar()
    print(carro)
    carro.frear()
    print(carro)
    carro.frear()
    print(carro)


if __name__ == "__main__":
    main()
