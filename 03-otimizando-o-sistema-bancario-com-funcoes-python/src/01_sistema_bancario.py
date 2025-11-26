"""
Objetivo Geral:
===============
Separar as funcionalidades existente de saque, depósito e extrato em funções.
Criar duas novas funções:
- cadastrar usuário (cliente); e
- cadastrar conta bancária

Desafio:
--------
Precisamos deixar nosso código mais modularizado, para isso, vamos criar funções
para as operações existentes>
- sacar
- depositar; e
- visualizar extrato.
Além disso, para a versão 2 do sistema, precisamos criar duas novas funções:
- criar usuário (cliente do banco); e
- criar conta corrente (vincular com usuário)

Separação em funções
--------------------
Devemos criar funções para todas as operações do sistema.
Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra
na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser 
definida por você da forma que achar melhor.

Saque
-----
A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão de argumentos:
- saldo
- valor, 
- extrato
- limite
- numero_saques
- limite_saques
Sugestão de retorno:
- saldo
- extrato

Depósito
--------
A função depósito deve receber os argumentos apenas por posição (positional 
only).
Sugestão de argumentos:
- saldo
- valor
- extrato
Sugestão de retorno:
- saldo
- extrato

Extrato
-------
A função extrato deve receber os argumentos por posição e nome (positional only 
e keyword only).
Argumentos posicionais:
- saldo
Argumentos nomeados:
- extrato

Novas funções
-------------
Precisamos criar duas novas funções:
- criar usuário; e
- criar conta corrente
Fique a vontade para adicionar mais funções, exemplo: listar contas.

Criar usuário (cliente)
-----------------------
O programa deve armazenar os usuários em uma lista, um usuário é composto por: 
- nome
- data de nascimento
- cpf
- endereço: É uma string com o formato:
    - logradouro
    - número
    - bairro
    - cidade/sigla uf.
Não podemos cadastrar 2 usuários com o mesmo cpf.

Criar conta corrente
--------------------
O programa deve armazenar contas em uma lista, uma conta é composta por:
- agência
- número da conta; e
- usuário
O número da conta é sequencial, iniciando em 1. O número da agência é fixo: 0001
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um 
usuário.

Dica
----
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o 
número do CPF, informando para cada usuário da lista.
"""


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor,
                extrato=extrato, limite=limite, numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            _extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, "
                + "por favor selecione novamente a operação desejada.")


def menu():
    return input("\n"
        + "[d] Depositar\n"
        + "[s] Sacar\n"
        + "[e] Extrato\n"
        + "[q] Sair\n\n"
        + "=> ")


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"        
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def _extrato(saldo, *, extrato):
    print()
    print(" Extrato ".center(42, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(42, "="))
    


if __name__ == "__main__":
    main()
