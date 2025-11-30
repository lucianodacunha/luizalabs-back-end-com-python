"""
1. Criar e escrever um arquivo de texto simples

Crie um arquivo chamado mensagem.txt e escreva nele uma frase de sua escolha
usando with open(). Depois, abra novamente o arquivo e exiba o conteúdo na tela.
"""

from pathlib import Path


def func1():
    curr_dir = Path(__file__).resolve().parent
    file_path = curr_dir / "mensagem.txt"

    try:
        with file_path.open(mode="w", encoding="utf-8", newline="") as f:
            print("Escrevendo o arquivo...")
            f.write("Hello World!")
        with file_path.open(mode="r", encoding="utf-8", newline="") as f:
            print("Lendo o arquivo...")
            texto = f.read()
        print(f"Conteúdo do arquivo: {texto}")
    except IOError as e:
        print(f"Falha ao abrir o arquivo: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")


func1()
