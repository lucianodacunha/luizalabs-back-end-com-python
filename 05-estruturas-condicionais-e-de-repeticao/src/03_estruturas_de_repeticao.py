"""
estrutura de repetição
"""

# for, iterando sobre uma lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

for item in lista:
    print(f"{item}", end=" ")

print()
print()

# iterando sobre uma string.
palavra = "Python"

for letra in palavra:
    print(f"{letra}", end="   ")

print()
print()

# range, gerando sequências.
for i in range(1, 6):
    print(f"{i}", end=" ")

print()
print()

# while
resp = "s"

while resp.lower() != "n":
    resp = input("Deseja continuar?[S/n]: ")

print("Fim do programa!")

print()


# while com break
resp = "s"

while True:
    resp = input("Deseja continuar?[S/n]: ")
    if resp.lower() == 'n':
        break

print("Fim do programa!")

print()


# for com continue, imprimindo pares.
for i in range(11):
    if i % 2 == 0:
        print(f"{i}", end=" ")
    else: continue

print()