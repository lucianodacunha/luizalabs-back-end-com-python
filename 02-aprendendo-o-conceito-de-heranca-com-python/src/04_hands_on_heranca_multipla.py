"""Herança multipla

Conceito avançado e importante que apesar de seus poderes, em muitos casos
podem ser desencorajado, em razão da sua alta complexidade que pode ocasionar
nas clases envolvidas.
Avalie com cuidado se ele é realmente necessário.
"""
class Animal:
    """Classe inicial da hierarquia
    """
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return (f"Tipo: {self.__class__.__name__}\n"
                + f"{", ".join([f'{c}: {v}' for c, v in self.__dict__.items()])}\n")

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        """ Construtor de Mamifero, recebera sempre primeiramente os parametros
        existentes na sua classe pai. Depois, os parametros da classe atual, que
        devem ser passados como kwargs e consequentemente, serem nomeados.
        """
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)



class Cachorro(Mamifero):
    ...


class Gato(Mamifero):
    ...


class Leao(Mamifero):
    ...


class Ornitorrinco(Ave, Mamifero):
    def __init__(self, **kwargs):
        """O __mro__ demonstra a ordem de execução dos objetos.
        """
        print(Ornitorrinco.__mro__)
        super().__init__(**kwargs)


def main():
    gato = Gato(numero_patas=4, cor_pelo="amarelo")
    print(gato)

    # Argumentos devem ser nomeados.
    orni = Ornitorrinco(numero_patas=4, cor_bico="marron", cor_pelo="amarelo")
    print(orni)


if __name__ == "__main__":
    main()
