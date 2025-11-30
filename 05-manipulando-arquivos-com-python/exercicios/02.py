"""
2. Ler um arquivo linha a linha (sem usar .read())
Dado um arquivo qualquer de texto longo (ex.: um pequeno texto literário), leia-o linha por linha usando um for e imprima as linhas numeradas:

1: primeira linha
2: segunda linha
...
Use strip() para limpar quebras de linha.
"""

from pathlib import Path

def func2():
    curr_dir = Path(__file__).resolve().parent
    file_path = curr_dir / "zen_of_python.txt"

    try:
        with file_path.open(mode="r", encoding="utf-8", newline="") as f:
            for numero, texto in enumerate(f, 1):
                print(f"{str(numero).zfill(2)}: {texto.strip()}")
    except IOError as e:
        print(f"Falha ao abrir o arquivo: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

func2()