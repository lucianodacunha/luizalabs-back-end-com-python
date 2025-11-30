"""
5. Criar e organizar diretórios com os ou pathlib
Crie um script que:

Cria uma pasta chamada projetos

Dentro dela, cria três subpastas:

entrada
processamento
saida
Liste todas as pastas criadas

Faça usando pathlib.
"""

from pathlib import Path

def func5():
    curr_dir = Path(__file__).resolve().parent
    projetos = curr_dir / "projetos"
    entrada = projetos / "entrada"
    processamento = projetos / "processamento"
    saida = projetos / "saida"

    try:
        Path.mkdir(projetos, exist_ok=True)
        print(f"Criando a pasta {projetos}")
        Path.mkdir(entrada, exist_ok=True)
        print(f"Criando a pasta {entrada}")
        Path.mkdir(processamento, exist_ok=True)
        print(f"Criando a pasta {processamento}")
        Path.mkdir(saida, exist_ok=True)
        print(f"Criando a pasta {saida}")

        print(f"Listando conteudo de {projetos}")
        for child in Path.iterdir(projetos):
            print(child)
    except FileExistsError as e:
        print(f"Falha ao criar diretório: {e}")
    except FileNotFoundError as e:
        print(f"Falha ao criar diretório: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")


func5()
