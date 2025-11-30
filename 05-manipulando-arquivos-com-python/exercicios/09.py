"""
9. Criar um CSV a partir de uma lista de dicionários
Dada uma lista:

dados = [
    {"nome": "Ana", "idade": 30},
    {"nome": "João", "idade": 25},
    {"nome": "Marcos", "idade": 40},
]
Crie um arquivo pessoas.csv com cabeçalhos e uma linha para cada pessoa.

Use DictWriter.
"""
import csv
from pathlib import Path

def func9():
    curr_dir = Path(__file__).resolve().parent
    csv_path = curr_dir / "pessoas.csv"
    campos = ["nome", "idade"]
    dados = [
        {"nome": "Ana", "idade": 30},
        {"nome": "João", "idade": 25},
        {"nome": "Marcos", "idade": 40},
    ]

    try:
        with open(file=csv_path, mode="w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()

            for registro in dados:
                writer.writerow(registro)
    except IOError as e:
        print(f"Falha ao manipular o arquivo: {e}")
    except Exception as e:
        print(f"Falha ao manipular o arquivo: {e}")


func9()
