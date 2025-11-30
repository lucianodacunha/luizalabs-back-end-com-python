
def calcular_imposto(salario):
    aliquota = 0.0
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100.01 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15

    return aliquota * salario


def main():
    valor_salario = float(input("Entre com o valor do salário bruto: "))
    valor_beneficios = float(input("Entre com o valro dos benefícios: "))

    valor_imposto = calcular_imposto(valor_salario)
    saida = valor_salario - valor_imposto + valor_beneficios
    print(f"Valor do salário a ser transferido: {saida: .2f}")

         
if __name__ == "__main__":
    main()
