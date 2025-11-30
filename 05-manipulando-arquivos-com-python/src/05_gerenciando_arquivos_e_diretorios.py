import csv
import os
from pathlib import Path

# gerenciamento de arquivos e diretórios
def dir1():
    # recuperando diretorio atual
    """
    falando novamente de introspeção, __file__ retorna o arquivo atual.
    Dessa forma, utilizando a lib os e seus métodos, é possível recuperar
    informações de diretórios, arquivos, etc.
    """
    caminho_do_arquivo_atual = os.path.abspath(__file__)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    nome_do_arquivo_atual = os.path.basename(os.path.abspath(__file__))
    print(caminho_do_arquivo_atual)
    print(diretorio_atual)
    print(nome_do_arquivo_atual)

    # composição de caminhos, paths
    file_path = os.path.join(diretorio_atual, "arquivos", "notas.txt")

    with open(file_path, "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())


# copiando, movendo e apagando arquivos
import shutil

def shutil1():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    file_path_ori = os.path.join(diretorio_atual, "arquivos", "notas.txt")
    file_path_des = os.path.join(diretorio_atual, "arquivos", "notas1.txt")
    file_path_des2 = os.path.join(diretorio_atual, "arquivos", "notas2.txt")
    
    shutil.copy(file_path_ori, file_path_des)
    shutil.move(file_path_ori, file_path_des2)
    

# trabalhando com arquivo de um jeito moderno
from pathlib import Path

def path1():
    # Com Path.cwd, não é preciso introspectar a variável __file__
    curr_dir = Path(__file__)
    modulo = "05-manipulando-arquivos-com-python"
    src = "src"
    arquivos = "arquivos"
    arquivo = "notas2.txt"
    file_path = curr_dir / modulo / src / arquivos / arquivo
    print(file_path.is_file())


def path2():
    curr_dir = Path(__file__).resolve().parent
    arquivos = "arquivos"
    arquivo = "notas2.txt"
    file_path = curr_dir / arquivos / arquivo
    print(file_path.is_file())
    print(file_path.exists())


def stem2():
    curr_dir = Path(__file__).resolve().parent
    arquivos = "arquivos"
    arquivo = "notas2.txt"
    file_Path = curr_dir / arquivos / arquivo
    print(file_Path)
    print(file_Path.parent)
    print(file_Path.name)
    print(file_Path.stem)
    print(file_Path.suffix)


def iterdir1():
    curr_dir = Path(__file__).resolve().parent
    arquivos = "arquivos"
    dir_files = curr_dir / arquivos

    for f in dir_files.iterdir():
        print(f)


def glob1():
    curr_dir = Path(__file__).resolve().parent
    arquivos = "arquivos"
    dir_files = curr_dir / arquivos

    for f in dir_files.glob("*.txt"):
        print(f)


def mkdir1():
    curr_dir = Path(__file__).resolve().parent
    arquivos = "arquivos"
    dir_files = curr_dir / arquivos
    novo_dir = curr_dir / arquivos / "novo_dir"
    Path(novo_dir).mkdir(parents=True, exist_ok=True)
