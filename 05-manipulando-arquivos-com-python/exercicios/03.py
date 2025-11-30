"""
3. Copiar o conteúdo de um arquivo para outro

Leia o conteúdo de um arquivo origem.txt e crie um arquivo copia.txt com o mesmo
conteúdo. Depois confirme que ambos têm exatamente o mesmo texto.
"""

import filecmp
import difflib
from pathlib import Path

def func3():
    curr_dir = Path(__file__).resolve().parent
    origem = curr_dir / "zen_of_python.txt"
    copia =  curr_dir / "copia.txt"

    try:
        print("Abrindo arquivo para leitura...")
        with origem.open(mode="r", encoding="utf-8", newline="") as o:
            print("Abrindo arquivo para escrita...")
            with copia.open(mode="w",encoding="utf-8", newline="") as c:
                print("Escrevendo o arquivo...")
                for linha in o:
                    c.write(linha)
                # para testar a lib diff, descomente o código abaixo.
                # c.writelines(["\n", "Linha adicional"])
    except IOError as e:
        print(f"Falha: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

    print("Cópia realizada com sucesso!")
    print("Comparando os arquivos 1 e 2...")

    if filecmp.cmp(origem, copia, shallow=False):
        print("Os arquivos são identicos.")
    else:
        print("Os arquivos são diferentes.")
        print("Identificando as diferenças...")
        with origem.open(mode="r", encoding="utf-8", newline="") as o:
            with copia.open(mode="r", encoding="utf-8", newline="") as c:
                origem_linhas = o.readlines()
                copia_linhas = c.readlines()

                diff = difflib.unified_diff(origem_linhas, copia_linhas,
                                            fromfile=origem.as_posix())
                for linha in diff:
                    print(f"Diferenças: {linha}")


func3()