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
    => logradouro, número - bairro - cidade/uf.
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
    usuarios = {}
    contas = {}

    while True:
        opcao = menu_conta()

        if opcao == "u": # Criar usuários
            usuarios, contas, _ = criar_usuario(usuarios, contas)
        elif opcao == "c": # Criar contas
            contas, _ = _criar_conta_corrente(contas, usuarios=usuarios)        
        elif opcao == "l": # Listar usuários
            listar_usuários(usuarios)
        elif opcao == "r": # Listar contas
            listar_contas(contas)
        elif opcao == "o": # Operar contas
            while True:

                opcao = menu_operacoes()


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
                    return

                else:
                    print("Opção inválida, "
                        + "por favor informe novamente a operação desejada.")
        elif opcao == "s": # Sair
            break
        else:
            print("Opção inválida, "
                + "por favor informe novamente a opção desejada.")


def menu_conta():
    return input("\n"
        + "=> Criar [u]suário\n"
        + "=> [c]riar conta\n"
        + "=> [l]istar usuários\n"
        + "=> Lista[r] contas\n"
        + "=> [o]perar contas\n"
        + "=> [s]air\n\n"
        + "=> ")


def menu_operacoes():
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


def deposito(saldo, valor, extrato, /):
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
    

def criar_usuario(usuarios, contas, /, conta=None):
    """Cria um usuário e caso nenhuma conta for informada, uma conta corrente
    será criada e associada ao usuário atual.
    """
    usuario = {}

    print("\nEntre com os dados do usuário: ")
    nome = input("    Nome: ")
    data_nascimento = input("    Data de nascimento: ")
    cpf = input("    CPF: ")
    print("    Entre com os dados do endereço do usuário: ")
    logradouro = input("        Logradouro: ")
    numero = input("        Número: ")
    bairro = input("        Bairro: ")
    cidade = input("        Cidade: ")
    uf = input("        UF: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"

    usuario[cpf] = {
        "nome": nome,
        "nascimento": data_nascimento,
        "endereco": endereco
    }

    if not conta:
        input("\nUsuário criado sem um conta associada."
                + " Pressione enter para criar uma conta corrente... ")
        contas, conta = _criar_conta_corrente(contas, usuario, usuarios)
        print(contas, conta)
        input("_")
        print("\nConta corrente criada com sucesso!\n")

    list(conta.values())[0]["usuario"] = cpf
    list(usuario.values())[0]["contas"] = conta
    usuarios.update(usuario)

    return usuarios, contas, usuario


def _criar_conta_corrente(contas, /, usuario={}, usuarios=None):
    """Cria conta corrente, caso nenhum usuário for informado, cria um usuário
    e associa a conta atual.
    """
    conta = {}
    numero = len(contas) + 1
    agencia = "0001"
    # usuario = None if not usuario else list(usuario.keys())[0]
    conta[numero] = {"agencia": agencia}

    print(f"\nConta criada com sucesso: {conta}")
    print()

    if not usuario:
        while True:
            opcao = input("Atribua um usuário à nova conta: "
                        + "\n   [i]nformar um usuário (CPF) existente:"
                        + "\n   [c]riar um novo usuário: "
                        + "\n"
                        + "\n   ==> ")
            if opcao == "i":
                cpf = input("Informe o CPF do usuário desta conta: ")
                if cpf in usuarios:
                    usuario = {}
                    usuario[cpf] = usuarios.get(cpf)
                    list(usuario.values())[0].get("contas").update(conta)
                    break
                else:
                    print("CPF não localizado!")
            elif opcao == "c":
                usuarios, contas, usuario = criar_usuario(usuarios, contas, 
                                                conta=conta)
                break
            else:
                print("Opção inválida, informe novamente...")

    cpf = list(usuario.keys())[0]
    list(conta.values())[0]["usuario"] = cpf
    contas.update(conta)

    return contas, conta


def listar_usuários(usuarios, /):
    cpfs = list(usuarios.keys())

    for cpf in cpfs:
        dados = usuarios.get(cpf)
        usuario = (f"Nome: {dados['nome']}, Nascimento: {dados['nascimento']}, "
                 + f"Endereço: {dados['endereco']}, CPF: {cpf}.")
        print(usuario)


def listar_contas(contas, /):
    numeros = list(contas.keys())

    for numero in numeros:
        dados = contas.get(numero)
        conta = (f"Número: {numero}, Agência: {dados['agencia']}, "
               + f"CPF:  {dados['usuario']}.")
        print(conta)


if __name__ == "__main__":
    main()
