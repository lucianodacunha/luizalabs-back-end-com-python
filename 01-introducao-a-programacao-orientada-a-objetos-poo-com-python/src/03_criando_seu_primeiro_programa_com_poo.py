"""
Crie um programa onde informe: cor, modelo, ano e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.tipo = self.__class__.__name__
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("buzinando...")

    def parar(self):
        print("parando...")

    def correr(self):
        print("correndo...")

    def __str__(self):
        return (f"{self.tipo}: \n"
                + f"\tCor: {b1.cor}, \n"
                + f"\tModelo: {b1.modelo}, \n"
                + f"\tAno: {b1.ano}, \n"
                + f"\tValor: {b1.valor}")


def main():
    b1 = Bicicleta("Azul", "Track", 2024, 2000.0)
    print(f"Bicicleta: \n"
          + f"\tCor: {b1.cor}, \n"
          + f"\tnModelo: {b1.modelo}, \n"
          + f"\tAno: {b1.ano}, \n"
          + f"\tValor: {b1.valor}")

    b1.correr()
    b1.buzinar()
    b1.parar()


if __name__ == "__main__":
    main()
