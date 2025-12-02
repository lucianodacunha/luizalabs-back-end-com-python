class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            print(f"depositando {valor}...")
            self.saldo += valor
            

    def sacar(self, valor):
        if (valor > 0) and (self.saldo - valor > 0):
            print(f"sacando {valor}...")
            self.saldo -= valor
    
    def __str__(self):
        return (f"Titular: {self.titular}, saldo: {self.saldo}")


def main():
    conta = ContaBancaria("Luciano", 1000.0)
    print(conta)
    conta.sacar(100.0)
    conta.depositar(300.0)
    print(conta)


if __name__ == "__main__":
    main()
