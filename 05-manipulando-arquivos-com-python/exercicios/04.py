"""
4. Criar um programa de "contador de palavras"

Peça ao usuário um nome de arquivo. O programa deve:

abrir o arquivo
contar quantas palavras existem
exibir o total
Use tratamento de exceções para:

arquivo não encontrado
arquivo vazio
permissões negadas
"""

from pathlib import Path


def func4():
    curr_dir = Path(__file__).resolve().parent
    _file = curr_dir / "zen_of_python.txt"
    linhas = {}
    palavras = 0

    with _file.open(mode="r", encoding="utf-8", newline="") as f:
        for numero, texto in enumerate(f, 1):
            linhas[f"{numero:02}"] = {f"{len(texto.split()): 03}": texto.split()}
            palavras += len(texto.split())

    for linha, valores in linhas.items():
        quantidade = list(valores.keys())[0]
        itens = ", ".join((list(valores.values()))[0])
        print(f"{linha}: {quantidade} | {itens}")

    print(f"Total de palavras: {palavras}")

func4()