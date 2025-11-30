import csv
import os
from pathlib import Path

# utilizando context manager
def open2():
    print("lendo o arquivo todo")
    with open(file_path, "r") as arquivo:
        print(arquivo.read())


# formas de leitura de um arquivo
def open3():
    print("lendo com readlines")
    with open(file_path, "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)


def open4():
    print("lendo com readline...")
    with open(file_path, "r") as arquivo:
        linha = arquivo.readline()
        while linha:
            print(linha, end="")
            linha = arquivo.readline()


def open5():
    print("lendo com for e strip")
    with open(file_path, "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())

