"""
7. Criar um programa que remove linhas duplicadas em um arquivo

Receba um arquivo .txt contendo várias linhas repetidas. Crie outro arquivo com 
somente linhas únicas, mantendo a ordem original.

Dicas:

use um conjunto (set) para rastrear duplicatas
cuidado para não alterar o arquivo original
"""

from pathlib import Path
from random import randint

FRASES = {
    2: 'The Zen of Python, by Tim Peters', 
    3: 'Beautiful is better than ugly.', 
    4: 'Explicit is better than implicit.', 
    5: 'Simple is better than complex.', 
    6: 'Complex is better than complicated.', 
    7: 'Flat is better than nested.', 
    8: 'Sparse is better than dense.', 
    9: 'Readability counts.', 
    10: 'Special cases aren\'t special enough to break the rules.', 
    11: 'Although practicality beats purity.', 
    12: 'Errors should never pass silently.', 
    13: 'Unless explicitly silenced.', 
    14: 'In the face of ambiguity, refuse the temptation to guess.', 
    15: 'There should be one-- and preferably only one --obvious way to do it.', 
    16: 'Although that way may not be obvious at first unless you\'re Dutch.', 
    17: 'Now is better than never.', 
    18: 'Although never is often better than *right* now.', 
    19: 'If the implementation is hard to explain, it\'s a bad idea.',         
}

def func7():
    curr_dir = Path(__file__).resolve().parent
    duplicado = curr_dir / "duplicado.txt"
    unico = curr_dir / "unico.txt"
    
    try:
        if not duplicado.exists():
            _cria_duplicado(duplicado)
        
            with duplicado.open(mode="r", encoding="utf-8", newline="") as d:
                linhas_unicas = set()
                for linha in d:
                    linhas_unicas.add(linha)

                with unico.open(mode="w", encoding="utf-8", newline="") as u:
                    u.writelines(linhas_unicas)
    except IOError as e:
        print(f"Falha: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")


def _cria_duplicado(duplicado):
    try:
        with duplicado.open(mode="w", encoding="utf-8", newline="") as f:
            for i in range(20):
                linha = randint(2, 19)
                f.write(f"{FRASES.get(linha, 1)}\n")
    except IOError as e:
        raise IOError(f"Falha: {e}")
    except Exception as e:
        raise Exception(f"Falha inesperada: {e}")

func7()
