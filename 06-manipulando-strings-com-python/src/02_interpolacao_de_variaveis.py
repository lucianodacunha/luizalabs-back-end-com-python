"""
Inteporlação de variáveis em strings.
"""

nome = "Greg"
idade = 24
pais = "Portugal"
altura = 1.75

template = f"Olá, meu nome é {nome}, tenho {idade} anos.\n"
template += f"Atualmente moro em {pais} e minha altura é {altura}m.\n"

print(template)

# Outras formas de interpolação.

# antigas
cidade = "São Paulo"
ano = 2025
print("Cidade atual %s, ano %d." % (cidade, ano))
print("Cidade atual {}, ano {}.".format(cidade, ano))
print("Cidade atual {0}, ano {1}.".format(cidade, ano))
print("Cidade atual {city}, ano {year}.".format(city=cidade, year=ano))

# formatando valores
saldo = 1450.32
print(f"Seu saldo é {saldo: .2f}")
