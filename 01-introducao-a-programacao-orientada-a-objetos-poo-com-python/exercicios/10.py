class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            print("depositando ...")
            self.saldo += valor

    def sacar(self, valor):
        if (self.saldo - valor) >= 0:
            print("sacando ...")
            self.saldo -= valor
        else:
            print(f"\nSaldo insuficiente!")

    def extrato(self):
        print(f"\nSaldo: {self.saldo}")


def main():
    conta = Conta(numero=1, titular="Luciano", saldo=12000.0)

    while True:
        op = input("\n[1] Depositar\n"
                   + "[2] Sacar\n"
                   + "[3] Extrato\n"
                   + "[4] Sair\n"
                   + "\n==> ")

        if op == "1":
            valor = float(input("\nEntre com o valor de depósito: "))
            conta.depositar(valor)
        elif op == "2":
            valor = float(input("\nEntre com o valor de saque: "))
            conta.sacar(valor)
        elif op == "3":
            conta.extrato()
        elif op == "4":
            print("...finalizando operação")
            break
        else:
            input("\nOpção inválida! Digite enter para continuar...")


if __name__ == "__main__":
    main()
