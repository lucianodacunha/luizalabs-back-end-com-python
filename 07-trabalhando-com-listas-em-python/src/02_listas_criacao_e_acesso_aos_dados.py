"""
Criação e acesso
"""

# declaração 
numeros = [1, 2, 3, 4, 5, 6]
palavras = ["python", "java", "c-sharp", "go", "koltin"]
valores = [1.32, 4.33, 6.34, 43.11, 12.44, 65.33]

# listas heterogeneas
misc = [1, "python", 1.32, "\U0001F600", 5j+1, True]

lista_vazia1 = []
lista_vazia2 = list()

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

# Acessando os elementos
print(numeros)
print(palavras)
print(valores)

print(palavras[-1])
print(palavras[-2])
print(numeros[::-1])

# alterado valores
print(palavras)
palavras[1] = "javascript"
print(palavras)

# utilizando loops para iterar na lista

for i in palavras:
    print(i, end=" ")

print()

for i in range(len(palavras)):
    print(palavras[i], end=" ")

print()