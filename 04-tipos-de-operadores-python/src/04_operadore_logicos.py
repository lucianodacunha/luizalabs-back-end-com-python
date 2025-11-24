"""
Operadores lógicos
"""

idade = input("Informe sua idade: ")
pagamento = input("Já realizou o pagamento?[S/N]: ")
valor = input("Qual o valor pago? ")

# Condições fracionadas para melhor entendimento, não trata erros de entrada.
maior_de_idade = (int(idade) >= 18)
pagamento_realizado = (pagamento.upper() == "S")
valor_correto = (float(valor) >= 2000.0) 

result = maior_de_idade and pagamento_realizado and valor_correto

print(f"Resultado: {result}")
