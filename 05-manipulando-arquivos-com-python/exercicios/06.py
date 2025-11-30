"""
6. Registrar logs simples em um arquivo

Implemente um programa que:

- recebe entradas do usuário em um loop
- salva cada entrada em logs.txt
- finaliza quando o usuário digitar "sair"

Cada linha do log deve estar no formato:

[2025-11-27 13:45:10] Usuario digitou: exemplo

Use datetime.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def log1():    
    template = f"[%(asctime)s] Usuario digitou: %(message)s"
    log_path = Path(__file__).resolve().parent / "log.log"
    logging.basicConfig(filename=log_path, format=template, level=logging.INFO)

    try:
        while True:
            entrada = input("Entre com um termo (q para sair): ")
            if entrada.lower() == "q":
                break
            logger.info(entrada)
    except Exception as e:
        print(f"Erro inesperado: {e}.")


log1()