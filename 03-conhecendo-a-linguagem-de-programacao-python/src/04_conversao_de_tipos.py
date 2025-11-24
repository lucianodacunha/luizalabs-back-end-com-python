"""
Conversão de tipos
"""

inteiro = 10
string = str(inteiro) # Convertendo para str

print(f"variavel inteiro: {type(inteiro)}, {inteiro}")
print(f"variavel string: {type(string)}, {string}")

_float = float(inteiro)

print(f"variavel _float: {type(_float)}, {_float}")

# Operações com tipos distintos

print(f"Soma: 10 + 10.0: {inteiro + _float}") # resulta em float

# resulta em TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(f"Soma: 10 + '10': {inteiro + string}") 

# resulta em concatenação
print(f"Soma: str(10) + '10': {str(inteiro) + string}") 

# Na divisão
print(inteiro / inteiro) # por padrão, a divisão retorna um float
print(32 // inteiro) # o op // retorna um inteiro
