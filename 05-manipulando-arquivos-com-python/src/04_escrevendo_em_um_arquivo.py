import csv
import os
from pathlib import Path

# escrevendo em uma arquivo
def write1():
    with open(file_path, "w") as arquivo:
        arquivo.write("Introdução a manipulação de arquivos\n")


# escrevendo em um arquivo, append
def write1():
    with open(file_path, "a") as arquivo:
        arquivo.write("Abrindo e fechando arquivos Lendo de um arquivo\n")


# escrevendo em um arquivo, multiplas linhas
def write2():
    lista = [
        "Escrevendo em um arquivo\n", 
        "Gerenciando arquivos e diretórios\n", 
        "Tratamento de exceções em manipulação de arquivos\n",
        "Boas práticas na manipulação de arquivos\n",
        "Trabalhando com arquivos CSV\n"
    ]

    with open(file_path, "a") as arquivo:
        arquivo.writelines(lista)

