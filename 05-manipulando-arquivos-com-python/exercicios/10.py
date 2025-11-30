"""
10. Criar um programa de “Relatório de Gastos” usando CSV

Crie um CSV chamado gastos.csv com as colunas:

descricao,valor
Depois escreva um script que:

lê o arquivo
soma todos os valores
monta um relatório como:
Relatório de Gastos
-------------------
Total de lançamentos: 7
Total gasto: R$ 1034.50
Esse exercício junta leitura de CSV, conversão de tipos e formatação.
"""

import csv
import random
from pathlib import Path


def func10():
    curr_dir = Path(__file__).resolve().parent
    csv_path = curr_dir / "gastos.csv"

    try:
        if not csv_path.exists():
            _cria_gastos(csv_path)
        with open(file=csv_path, mode="r", encoding="utf-8", newline="") as f:
            lancamentos = 0
            gastos = 0.0
            reader = csv.DictReader(f)
            print("".center(50, "="))
            print(" Relatório de Gastos ".center(50, " "))
            print("".center(50, "="))
            for row in reader:
                lancamentos += 1
                gastos += float(row['valor'])
                print(f"{str(row['descricao']).capitalize():<25} " 
                    + f"R$ {float(row['valor']): .2f}")
            print("".center(50, "-"))
            print(f"{'Total de gastos':<25} R$ {gastos: .2f}")
            print(f"{'Total de lançamentos':<25} {lancamentos}")
            print("".center(50, "="))
    except IOError as e:
        print(f"Falha ao manipular o arquivo: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

def _cria_gastos(csv_path):
    campos = ["descricao", "valor"]
    gastos = [
        {"descricao": "alimentacao", "valor": 600.54},
        {"descricao": "farmacia", "valor": 200.43},
        {"descricao": "transporte", "valor": 400.01},
        {"descricao": "educacao", "valor": 700.33},
        {"descricao": "lazer", "valor": 300.10},
    ]

    with open(file=csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()

        for registro in gastos:
            writer.writerow(registro)


func10()
