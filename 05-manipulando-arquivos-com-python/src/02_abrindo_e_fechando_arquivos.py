import csv
import os
from pathlib import Path

# abrindo e fechando arquivos
def open1():
    arquivo = open(file_path, "r")
    # lendo 
    print(arquivo.read())
    #fechando
    arquivo.close()

