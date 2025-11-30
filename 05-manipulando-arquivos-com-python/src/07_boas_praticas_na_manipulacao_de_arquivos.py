import csv
import os
from pathlib import Path

# prefira utilizar gerenciador de context para abrir 
# trate as exceções o máximo possível
# dê preferência criar caminhos com Path
# Evite utilizar read() para ler arquivo que podem ser grandes
# documente o encoding
# cuidado ao utilizar mode="w", evitando sobrescrver arquivos
def with1():
    Path(__file__).resolve().parent
    curr_dir = Path(__file__).resolve().parent
    # a barrra implementa o join do modulo os.path
    file_path = curr_dir / "arquivos" / "dados.txt"
   
    try:
        if file_path.is_file():
            with file_path.open(mode="r", encoding="utf-8") as f:
                for linha in f:
                    print(linha, end="")
        else:
            print(f"O path {file_path} não é um arquivo válido.")
    except IOError as e:
        print(f"Falha ao abrir o arquivo: {e}")
    except Exception as e:
        print(f"Exception inesperada: {e}")
    finally:
        # nesse caso, finally é dispensável, o with está fechando o arquivo.
        ...


if __name__ == "__main__":
    with1()
