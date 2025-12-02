class Aluno:
    def __init__(self, nome, /, *notas):
        self.nome = nome
        self.notas = notas

    def media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"

    def __str__(self):
        notas = ", ".join(map(lambda x: str(x), self.notas))
        return (f"Nome: {self.nome}, Notas: {notas}")


def main():
    a = Aluno("Luciano", 7, 8, 9.5, 10, 9, 8.5)
    print(a)
    print(f"Média: {a.media(): .2f}")
    print(f"Situação: {a.situacao()}")


if __name__ == "__main__":
    main()
