class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor =  cor
        self.placa =  placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"Ligando o motor do {self.__class__.__name__}")

    def __str__(self):
        return (f"Tipo: {self.__class__.__name__}\n" 
                + f"Cor: {self.cor}\n"
                + f"Placa: {self.placa}\n"
                + f"Número de Rodas: {self.numero_rodas}\n")


class Motocicleta(Veiculo):
    ...


class Carro(Veiculo):
    def ligar_motor(self):
        print(f"Ligando o motor do {self.__class__.__name__}")



class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        return "Sim\n" if self.carregado else "Não\n"


def main():
    moto = Motocicleta(cor="preta", placa="ABC-1234", numero_rodas=2)
    carro = Carro(cor="preta", placa="BCD-2211", numero_rodas=4) 
    caminhao = Caminhao("azul", "RDF-2233", 6, True)
    
    print(moto)
    print(carro)
    print(caminhao)

    moto.ligar_motor()
    carro.ligar_motor()
    caminhao.ligar_motor()

    # print(f"Está carregado: {caminhao.esta_carregado()}")

if __name__ == "__main__":
    main()
