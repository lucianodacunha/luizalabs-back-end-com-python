"""
Alguns métodos da classe dict
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

# acessando valores
print(data.get("nome"))

# acessar com get não gerar erro caso a chave não existir
print(data.get("altura"))

# podemos verificar com o operador in, se a chave existe.
print(f"{'carro' in data}")

# removendo valores
cidade = data.pop("cidade")
print(data)
print(cidade)

data["cidade"] = "Campinas"
print(data)

data.popitem()
print(data)

data["cidade"] = "Campo Grande"
print(data)

del data["cidade"]
print(data)

# atualiza se existe, caso contrário insere.
data.update({"cidade": "Salvador", "nome": "Lais"})
print(data)

# copia o valor do objeto
data4 = data.copy()
data5 = data4
print(data4)
print(data5)

# atualiza valores
data4.update({"nome": "Simone", "idade": 43})
print(data)
print(data4)
print(data5)

# limpa dicionário
data4.clear()
print(data)
print(data4)
print(data5)

# iteração
for chave, valor in data.items():
    print(chave, valor)
