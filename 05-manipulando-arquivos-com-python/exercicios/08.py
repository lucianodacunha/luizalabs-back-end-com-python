"""
8. Processar um arquivo CSV lendo valores como dicionários
Dado um CSV com cabeçalho:

nome,idade,cidade
Leia o arquivo usando csv.DictReader e exiba na tela frases como:

Ana tem 30 anos e mora em São Paulo.
"""

import csv
import random
from random import randint
from pathlib import Path

def func8():
    curr_dir = Path(__file__).resolve().parent
    csv_path = curr_dir / "customers.csv"

    try:
        if not csv_path.exists():
            _criar_csv_path(csv_path)

        with open(file=csv_path, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['nome']} tem {row['idade']} anos de idade e mora em " 
                    + f"{row['cidade']}.")
    except IOError as e:
        print(f"Falha ao manipular o arquivo: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

def _criar_csv_path(csv_path):
    CAMPOS = ["nome", "idade", "cidade"]
    NOMES = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Giovana',
             'Hugo', 'Isabela', 'Joao']
    CIDADES = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 
               'Salvador', 'Recife', 'Curitiba']

    with open(file=csv_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()

        for i in range(10):
            registro = {
                "nome": NOMES[i],
                "idade": randint(18, 70),
                "cidade": random.choice(CIDADES)
            }
            print(registro)

            writer.writerow(registro)


func8()
