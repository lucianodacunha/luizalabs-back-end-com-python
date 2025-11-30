import csv
import os
from pathlib import Path

# Tratando exceções em manipulação de arquivos.
def except1():
    try:
        curr_dir = Path(__file__).resolve().parent
        file_path = (curr_dir / "arquivos" / "notas1.txt")
        with open(file_path) as arquivo:
            print(arquivo.read())
    except FileNotFoundError as e:
        print(f"{e}")
    except PermissionError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Erro Inesperado: {e}")


def except2():
    """-rw-r----- 1 root    root      20 nov 30 08:11 arquivo-confidencial

    """
    try:
        curr_dir = Path(__file__).resolve().parent
        file_path = (curr_dir / "arquivos" / "arquivo-confidencial")
        with open(file_path, "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError as e:
        print(f"{e}")
    except IsADirectoryError as e:
        print(f"{e}")
    except NotADirectoryError as e:
        print(f"{e}")
    except PermissionError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Erro Inesperado: {e}")

