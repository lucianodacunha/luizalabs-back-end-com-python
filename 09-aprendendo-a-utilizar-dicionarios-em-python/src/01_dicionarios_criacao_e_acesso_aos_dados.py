"""
Dicionários
"""

# criação
data = {
    "nome": "Gael",
    "idade": 30,
    "cidade": "Curitiba"
}

# criacao de dict com construtor
data2 = dict() # vazio
data3 = dict(nome="Paula", idade=40, cidade="Passos")

# acesso simples de valores
print(data3["nome"])

# alterando valores
data["cidade"] = "Londrina"
print(data)
