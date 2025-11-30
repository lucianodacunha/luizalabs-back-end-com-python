import csv
import os
from pathlib import Path

# escrevendo um csv
def csv1():
    curr_dir = Path(__file__).resolve().parent
    file_path = (curr_dir / "arquivos" / "tabela.csv")

    with open(file_path, "w", newline="") as f:
        esc = csv.writer(f)
        esc.writerow(["id", "cidade"])
        esc.writerow([1, "São Paulo"])
        esc.writerow([2, "Rio de Janeiro"])
        esc.writerow([3, "Salvador"])


# lendo um csv
def csv2():
    curr_dir = Path(__file__).resolve().parent
    file_path = (curr_dir / "arquivos" / "tabela.csv")

    with open(file_path, "r", newline="") as f:
        lei = csv.reader(f)
        for linha in lei:
            print(linha)


# usando dictreader/writer
def dict1():
    curr_dir = Path(__file__).resolve().parent
    file_path = (curr_dir / "arquivos" / "tabela.csv")

    with open(file_path, "r", newline="") as f:
         for linha in lei:
            print(linha["id"], linha["cidade"])    


# escrevendo um csv com dictwriter
def dict2():
    curr_dir = Path(__file__).resolve().parent
    file_path = (curr_dir / "arquivos" / "tabela.csv")

    with open(file_path, "w", newline="") as f:
        field_names = ["id", "cidade"]
        esc = csv.DictWriter(f, fieldnames=field_names)

        esc.writeheader()
        esc.writerow({"id": 1, "cidade":"São Paulo"})
        esc.writerow({"id": 2, "cidade":"Rio de Janeiro"})
        esc.writerow({"id": 3, "cidade":"Salvador"})


if __name__ == "__main__":
    dict2()
