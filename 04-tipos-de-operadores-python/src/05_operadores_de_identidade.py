palavra = "python"
linguagem = palavra

print(f"{palavra is linguagem}")

"""
lower(self, /) unbound builtins.str method
    Return a copy of the string converted to lowercase. <=== retorna uma cópia!
"""
python = linguagem.lower()

print(f"{python is linguagem}")
print(f"{python is not linguagem}")

# Verificando o id ou região de memória de cada variável
print(f"{id(python)}")
print(f"{id(linguagem)}")
print(f"{id(palavra)}")
