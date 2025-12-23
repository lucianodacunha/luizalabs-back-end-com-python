"""
Utilizando a função explain do Copilot.

> Original:

This code defines a REST API endpoint using FastAPI that retrieves bank account statement information. The endpoint responds to HTTP GET requests at the URL path /contas/{numero_conta}/extrato, where {numero_conta} is a dynamic path parameter that captures the account number from the URL.

When a client makes a request to this endpoint, FastAPI automatically extracts the account number from the URL and passes it to the extrato function as a string parameter. The function first loads all account data by calling carregar_dados(), which reads from a JSON file and returns a dictionary structure containing all accounts under a "contas" key.

The function then performs a validation check to ensure the requested account exists. If the numero_conta is not found in the loaded data's accounts dictionary, it raises an HTTPException with a 404 status code and a Portuguese error message indicating the account was not found. This is the proper way to handle "resource not found" scenarios in REST APIs, as it immediately terminates execution and returns an appropriate HTTP error response to the client.

If the account exists, the function retrieves the full account object from the dictionary and constructs a response containing three pieces of information: the account holder's name (usuario), the transaction history (extrato), and the current balance (saldo). FastAPI automatically serializes this dictionary into JSON format and sends it back to the client with a 200 OK status code.

One potential gotcha here is that there's no error handling for cases where the account data structure might be malformed or missing expected fields. If conta["usuario"], conta["extrato"], or conta["saldo"] don't exist, the function will raise a KeyError and return a 500 Internal Server Error instead of a more informative client error. Additionally, loading data from a file on every request can become a performance bottleneck as the application scales—consider implementing caching or using a proper database solution for production environments.

> Retorno resumido em português:

Este endpoint da API retorna o extrato bancário de uma conta específica. Quando um cliente acessa api.py:110, a função carrega os dados do arquivo JSON e verifica se a conta existe. Se a conta não for encontrada, retorna um erro 404. Caso contrário, retorna um objeto JSON contendo o nome do usuário, o histórico de transações (extrato) e o saldo atual da conta.

A função utiliza o número da conta como parâmetro dinâmico na URL para identificar qual conta deve ser consultada no dicionário de dados carregado.

"""

import json
import os
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

ARQUIVO = "dados.json"

app = FastAPI(title="Sistema Bancário API")

# --------------------
# Persistência
# --------------------

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {"contas": {}}

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

# --------------------
# Schemas (contratos)
# --------------------

class ContaCreate(BaseModel):
    usuario: str

class Operacao(BaseModel):
    valor: float

# --------------------
# Endpoints
# --------------------

@app.post("/contas")
def criar_conta(dados_conta: ContaCreate):
    dados = carregar_dados()

    numero_conta = str(random.randint(10_000_000_000, 99_999_999_999))
    saldo_inicial = random.randint(100, 500)

    dados["contas"][numero_conta] = {
        "usuario": dados_conta.usuario,
        "saldo": saldo_inicial,
        "limite": 500,
        "extrato": []
    }

    salvar_dados(dados)

    return {
        "mensagem": "Conta criada com sucesso",
        "conta": numero_conta,
        "saldo_inicial": saldo_inicial
    }

@app.get("/contas/{numero_conta}")
def consultar_conta(numero_conta: str):
    dados = carregar_dados()

    if numero_conta not in dados["contas"]:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    return dados["contas"][numero_conta]

@app.post("/contas/{numero_conta}/deposito")
def depositar(numero_conta: str, operacao: Operacao):
    dados = carregar_dados()

    if numero_conta not in dados["contas"]:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if operacao.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    conta = dados["contas"][numero_conta]
    conta["saldo"] += operacao.valor
    conta["extrato"].append(f"+ R${operacao.valor:.2f}")

    salvar_dados(dados)

    return {"mensagem": "Depósito realizado", "saldo": conta["saldo"]}

@app.post("/contas/{numero_conta}/saque")
def sacar(numero_conta: str, operacao: Operacao):
    dados = carregar_dados()

    if numero_conta not in dados["contas"]:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    conta = dados["contas"][numero_conta]

    if operacao.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    if operacao.valor > conta["saldo"]:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    conta["saldo"] -= operacao.valor
    conta["extrato"].append(f"- R${operacao.valor:.2f}")

    salvar_dados(dados)

    return {"mensagem": "Saque realizado", "saldo": conta["saldo"]}

@app.get("/contas/{numero_conta}/extrato")
def extrato(numero_conta: str):
    dados = carregar_dados()

    if numero_conta not in dados["contas"]:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    conta = dados["contas"][numero_conta]

    return {
        "usuario": conta["usuario"],
        "extrato": conta["extrato"],
        "saldo": conta["saldo"]
    }

@app.post("/reset")
def resetar_sistema():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)

    return {"mensagem": "Sistema resetado com sucesso"}
