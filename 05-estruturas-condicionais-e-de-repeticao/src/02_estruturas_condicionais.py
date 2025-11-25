"""
Estruturas condicionais
"""

# if, else

saldo = 2000.0

saque = float(input("Entre com o valor do saque: "))

if saque <= saldo:
    print("Saque permitido")
else:
    print("Saque insuficiente")


print()
print()

# if, elif, else
temperatura = float(input("Entre com a temperatura: "))

if temperatura >= 40:
    print("Quente")
elif temperatura >= 30: 
    print("Ameno")
else:
    print("Frio")

print()
print()

# if ternário
IDADE_MINIMA = 18
idade_atual = int(input("Entre com sua idade: "))

entrada = "Sim" if idade_atual >= IDADE_MINIMA else "Não"
print(f"Entrada permitida? {entrada}")
