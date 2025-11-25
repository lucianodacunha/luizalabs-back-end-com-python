# Exemplo de uso de indentação:

# Blocos if

if True:
    print(True)
else:
    print(False)


# Código somente 'ilustrativo'
if False:
    if True:
        if False:
            return
        else:
            True
    else:
        False
elif True:
    return
else:
    return


# Função com if em sua estrutura
def imprimir(texto):
    conteudo = texto
    if conteudo is None:
        print("Nada a imprimir")
    else:
        print(f"Texto a imprimir: {texto}")


# Esse código não faz parte da função
print("Código sem função!")
