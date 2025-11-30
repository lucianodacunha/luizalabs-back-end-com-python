import csv
import os
from pathlib import Path

# Manipulação de arquivos em Python
# tudo começa com a função open
def open0():
    file_path = r".../dados.txt"
    arquivo = open(file_path, "r")
