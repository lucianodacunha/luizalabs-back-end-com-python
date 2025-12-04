class Conta:
    def __init__(self, saldo=0):
        """ Utiliza-se o _ antes do nome da variável, indicando que ela não deve
        ser acessar externamente, porém isso não impede o acesso.
        """
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def exibir_saldo(self):
        return self._saldo


c = Conta(1000.0)
# Isso é permitido, mas não recomendado.
print(c._saldo)

# Essa forma é mais recomendada
print(c.exibir_saldo())