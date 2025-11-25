"""
Métodos da classe list
"""

# declaração 
numeros = [1, 2, 3, 4, 5, 6]
palavras = ["python", "java", "c-sharp", "go", "koltin"]
valores = [1.32, 4.33, 6.34, 43.11, 12.44, 65.33]

# listas heterogeneas
misc = [1, "python", 1.32, "\U0001F600", 5j+1, True]

print(numeros)
numeros.append(10)
print(numeros)

# copia a referência
numeros2 = numeros 

# copia os valores
geral = numeros.copy()

# verificando se são os mesmos objetos
print(id(numeros), id(geral), id(numeros2))

# join entre duas listas
geral.extend(palavras)
print(geral)

# inserindo um valor
geral.insert(1, "computador")
print(geral)

# removendo item pelo valor
geral.remove("python")
print(geral)

# removendo item pelo indice
geral.pop(1)
print(geral)

# limpando a lista
geral.clear()
print(geral)

geral.extend(numeros)
geral.extend(misc)
print(geral)

# conta o numeros de ocorrencias
print(geral.count(1))

# retorna o indice do item
print(geral.index("python"))

# ordenação
# print(geral.sort()) não suportado entre int e str
valores2 = valores.copy()
print(valores2)
print(sorted(valores2))
valores2.sort()
print(valores2)

# outros métodos
numeros2 = numeros.copy()
print(numeros2)
numeros2.reverse()
print(numeros2)

# criação de listas com list comprehensions

l = [i for i in range(0, 11, 2)]
print(l)

x = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(x)
