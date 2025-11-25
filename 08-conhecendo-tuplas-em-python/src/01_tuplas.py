"""
Tuplas
"""

# DECLARAÇÃO
tupla = (1, 2, 3, 4, 5)
dados = ("Paulo", 32, 1.70, True, ["Pedro", "Bruna", "Larissa"])

print(tupla)
print(dados)

print(type(tupla))

# tuplas são imutáveis, mas seus objetos são mutáveis.
# dados[2] = 1.80, TypeError
# Aqui, estamos alterando o valor de um objeto, mas não o objeto.
dados[4][1] = "João"
print(dados)

# essa declaração não declara uma tupla
valor = (1)
print(type(valor))

# para declarar uma tupla, é importante declarar a virgula, até mais que os 
# parenteses
tupla_de_um_elemento = (1, )
print(type(tupla_de_um_elemento))

tupla_de_dois_elementos = 1, 2, 
print(type(tupla_de_dois_elementos))

# acessando elementos
print(tupla[::-1])

# desempacotamento
a, b = tupla_de_dois_elementos
print(a, b)

c, *d, e = tupla
print(c, d, e)

# MÉTODOS

# quantidade de ocorrências de um valor
print(tupla.count(2))

# indice de um valor
print(tupla.index(3))