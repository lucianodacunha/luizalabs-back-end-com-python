lista = [1, 2, 3, 4, 5]

def gerador(lista):
    for i in lista:        
        yield f"passando pelo gerador, {i}"

for i in gerador(lista):
    print(f"{i}, passando pelo for")
