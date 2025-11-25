"""
String multilinhas
"""

texto = """Lorem Ipsum is simply dummy text of the printing and
    typesetting industry. Lorem Ipsum has been the industry's standard 
    dummy text ever since the 1500s, when an unknown printer took a galley
    of type and scrambled it to make a type specimen book. It has survived
    not only five centuries, but also the leap into electronic 
    typesetting, remaining essentially unchanged."""


# imprime conforme formatação.
print(texto)

# fazenda menus
menu = """
    Entre com a opção desejada:
    1 - Ver saldo
    2 - Depositar
    3 - Sacar
    4 - Sair"""

print(menu)

# Também aceita interpolação
op1 = "1 - Ver saldo"
op2 = "2 - Depositar"
op3 = "3 - Sacar"
op4 = "4 - Sair"

menu = f"""
    Entre com a opção desejada:
    {op1}
    {op2}
    {op3}
    {op4}"""

print(menu)